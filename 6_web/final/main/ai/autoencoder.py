import os
import io
import json
import distutils.dir_util
import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
from itertools import chain 

# json write & load 함수 정의
def write_json(data, fname):
    def _conv(o):
        if isinstance(o, (np.int64, np.int32)):
            return int(o)
        raise TypeError

    parent = os.path.dirname(fname)
    distutils.dir_util.mkpath(parent)
    with io.open(fname, "w", encoding="utf-8") as f:
        json_str = json.dumps(data, ensure_ascii=False, default=_conv)
        f.write(json_str)
        
def load_json(fname):
    with open(fname, encoding='utf-8') as f:
        json_obj = json.load(f)

    return json_obj

# data load
path = os.getcwd()
path = path + '\\main\\ai\\data\\'
data_path = path + 'data.json'
mfl_col_path = path + 'mfl_col.pkl'
model_path = path + 'model_7.h5'

with open(mfl_col_path, 'rb') as f: # 사용 feature
    features = pickle.load(f)

data = pd.read_json(data_path) # 전체 플리 데이터

autoencoder = tf.keras.models.load_model(model_path)

# 1. ply_id 넣으면 해당 행을 원핫 벡터로 변경
def ply_to_onehot(select_ply_lst):
    # ply_id int형 변환
    select_ply_lst = list(map(int, select_ply_lst))
    # zero_mt 생성
    zero_matrix = np.zeros((1,len(features)))
    input_onehot = pd.DataFrame(zero_matrix,columns=features)

    # input_ply
    input_song = []
    input_tag = []
    for ply_id in select_ply_lst:
        input_song.append(data[data['id']==ply_id]['songs'].tolist()[0])
        input_tag.append(data[data['id']==ply_id]['tags'].tolist()[0])

    input_song = list(chain.from_iterable(input_song))
    input_tag = list(chain.from_iterable(input_tag))
    input_ply = input_song + input_tag

    # one-hot encoding
    for ft in input_ply :
        if ft in features:
            input_onehot.iloc[0,features.index(ft)]=1

    return input_song, input_tag, input_onehot

# 추천 결과 생성
def remove_seen(seen, l):
    seen = set(seen)
    return [x for x in l if not (x in seen)]

def recommendation(input_song, input_tag, input_onehot, song_num, tag_num=5, song_len=22798):
    # predict
    predict_plist = autoencoder.predict(input_onehot)

    # result
    ori_song = features[:song_len]
    ori_tag = features[song_len:]
    song_predict = predict_plist[:,:song_len] # song output(추천곡)
    tag_predict = predict_plist[:,song_len:] # tag output(추천태그)

    p_song = np.array(ori_song)[song_predict[0].argsort()[::-1][:(song_num*10)]]
    p_tag = np.array(ori_tag)[tag_predict[0].argsort()[::-1][:(tag_num*10)]]

    rec_song = remove_seen(input_song, p_song)[:song_num] 
    rec_tag = remove_seen(input_tag, p_tag)[:tag_num]
    
    return rec_song, rec_tag

# 유사도 적용
def apply_sim(similarity, input_song, rec_song, song_num):
    sim_num = round(song_num * (similarity / 100))
    rec_song = rec_song[:-sim_num]
    sim_song = input_song[:sim_num]
    sim_rec_song = sim_song + rec_song
    return sim_rec_song