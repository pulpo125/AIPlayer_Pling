from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm

model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')

def encoding(new_title):
    new_embedding=model.encode(new_title)
    return new_embedding

# 코사인 유사도
def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

# 임베딩 값 str->array 변환
def emd_to_array(ply_title_embedding):
   emd_array=ply_title_embedding.apply(lambda x: np.fromstring(x['ply_title_emd'].strip('[]'),dtype=float, sep=' '), axis=1)
   return emd_array

# 가장 유사한 플리 id list 추출하는 함수
def get_sim_ply_id(ply_title_embedding,new_embedding,n=2):
   ply_title_embedding['cos_sim'] = ply_title_embedding.apply(lambda x: cos_sim(x['ply_title_emd'], new_embedding), axis=1)
   sim_ply_id = list(ply_title_embedding.sort_values(by='cos_sim', ascending=False)['ply_id'][:2])
   return sim_ply_id