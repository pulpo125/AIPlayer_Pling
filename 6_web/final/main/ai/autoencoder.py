import pandas as pd
import numpy as np
import tensorflow as tf
from collections import Counter
# pip install tensorflow

data = './train.json'
model = './autoencoder_denoise_ad.h5'
autoencoder = tf.keras.models.load_model(model)

def load_data(data, like_cnt) :
    f = pd.read_json(data ,typ = 'frame', encoding='utf-8')
    df = pd.DataFrame(f)
    df = df.sort_values(by=['like_cnt'],ascending=False)
    df = df[df['like_cnt']>like_cnt]
    return df

# df loading
df = load_data(data, 5)

def make_features(song_num, tag_num) :
    # 플레이리스트 내 song id 리스트
    song_all = df['songs']
    # 플레이리스트 내 tag 리스트
    tag_all = df['tags']
    # 플레이리스트 내 song id 리스트 전체 나열
    song_list = [song for plist in song_all for song in plist]
    # 플레이리스트 내 tag 리스트 전체 나열
    tag_list = [tag for plist in tag_all for tag in plist]

    # 전체 나열 리스트 중 각 song의 개수
    count_song = Counter(song_list)
    # 전체 나열 리스트 중 각 tag의 개수
    count_tag = Counter(tag_list)

    meaningful={} 
    for key, value in count_song.items():
        if value>song_num:
            meaningful[key]=value
    song_len = len(meaningful) # 20회 넘게 담긴 song의 개수
    # 전체 플레이리스트 내 10회 넘게 담긴 tag을 dictionary에 추가
    for key, value in count_tag.items():
        if value>tag_num:
            meaningful[key]=value
    features = list(meaningful.keys()) # 유의미한 song과 tag 전체 개수

    return features, song_len

def ply_to_onehot(pl_id, features):
    zero_matrix=np.zeros((1,len(features)))
    onehot=pd.DataFrame(zero_matrix,columns=features)
    pl_ft = df[df['id']==pl_id]['songs'].tolist()[0] + df[df['id']==pl_id]['tags'].tolist()[0]

    for ft in pl_ft :
        if ft in features:
            onehot.iloc[0,features.index(ft)]=1

    return onehot

def recommendation(onehot, features, song_len, song_num, tag_num) :
    # autoencoder = tf.keras.models.load_model(model)
    predict_plist = autoencoder.predict(onehot)

    ori_song = features[:song_len]
    ori_tag = features[song_len:]
    song_predict = predict_plist[:,:song_len] # song output(추천곡)
    tag_predict = predict_plist[:,song_len:] # tag output(추천태그)

    p_song = np.array(ori_song)[song_predict[0].argsort()[-song_num:]] # predict한 song output 중 상위 n개
    p_tag = np.array(ori_tag)[tag_predict[0].argsort()[-tag_num:]]

    return p_song, p_tag