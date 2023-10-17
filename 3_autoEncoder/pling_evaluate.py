import os
import io
import json
import distutils.dir_util
import numpy as np

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

# 결과 추출 함수
def remove_seen(seen, l):
    seen = set(seen)
    return [x for x in l if not (x in seen)]

def generate_result(q_test, mfl_col, song_len, predict_plist):
    df_id = list(q_test['id']) # q_test ply_id 값 list 형태로 반환
    col= mfl_col # feature로 쓴 컬럼 값

    ori_song = col[:song_len] # mfl_col에서 song 값만 자르기
    ori_tag = col[song_len:] # mfl_col에서 tag 값만 자르기

    song_predict = predict_plist[:,:song_len] # song output(추천곡)
    tag_predict = predict_plist[:,song_len:] # tag output(추천태그)

    result=[]
    n=0
    for i in df_id: # q_test ply_id 값
        dic={}
        dic['id']=i # dic{'id':각 플리 id}

        plist_song = song_predict[n].argsort()[-200:] # predict한 song output 중 상위 200개
        p_song=[]
        for song in plist_song[::-1]:
            p_song.append(ori_song[song])
        dic['songs']=p_song

        plist_tag=tag_predict[n].argsort()[-100:] # predict한 tag output 중 상위 100개
        p_tag=[]
        for tag in plist_tag[::-1]:
            p_tag.append(ori_tag[tag])
        dic['tags']=p_tag
        n+=1
        result.append(dic)

    # remove_seen 적용
    questions = q_test[['id', 'tags', 'songs']].to_dict(orient='records')

    answers = []
    for i in range(len(result)):
        answers.append({
            "id": result[i]['id'],
            "songs": remove_seen(questions[i]["songs"], result[i]['songs'])[:100], 
            "tags": remove_seen(questions[i]["tags"], result[i]['tags'])[:10],
        })
    
    return answers

# 평가 클래스 정의
class ArenaEvaluator:
    def _idcg(self, l):
        return sum((1.0 / np.log(i + 2) for i in range(l)))

    def __init__(self):
        self._idcgs = [self._idcg(i) for i in range(101)]

    def _ndcg(self, gt, rec):
        dcg = 0.0
        for i, r in enumerate(rec):
            if r in gt:
                dcg += 1.0 / np.log(i + 2)
        if len(gt)>100:
            gt = gt[:100]
        return dcg / self._idcgs[len(gt)]

    def _eval(self, gt_fname, rec_fname):
        gt_playlists = load_json(gt_fname)
        gt_dict = {g["id"]: g for g in gt_playlists}
        rec_playlists = load_json(rec_fname)
        gt_ids = set([g["id"] for g in gt_playlists])
        rec_ids = set([r["id"] for r in rec_playlists])
        if gt_ids != rec_ids:
            raise Exception("결과의 플레이리스트 수가 올바르지 않습니다.")

        rec_song_counts = [len(p["songs"]) for p in rec_playlists]
        rec_tag_counts = [len(p["tags"]) for p in rec_playlists]
        if set(rec_song_counts) != set([100]):
            raise Exception("추천 곡 결과의 개수가 맞지 않습니다.")

        if set(rec_tag_counts) != set([10]):
            raise Exception("추천 태그 결과의 개수가 맞지 않습니다.")

        rec_unique_song_counts = [len(set(p["songs"])) for p in rec_playlists]
        rec_unique_tag_counts = [len(set(p["tags"])) for p in rec_playlists]

        if set(rec_unique_song_counts) != set([100]):
            raise Exception("한 플레이리스트에 중복된 곡 추천은 허용되지 않습니다.")

        if set(rec_unique_tag_counts) != set([10]):
            raise Exception("한 플레이리스트에 중복된 태그 추천은 허용되지 않습니다.")

        music_ndcg = 0.0
        tag_ndcg = 0.0

        for rec in rec_playlists:
            gt = gt_dict[rec["id"]]
            music_ndcg += self._ndcg(gt["songs"], rec["songs"][:100])
            tag_ndcg += self._ndcg(gt["tags"], rec["tags"][:10])

        music_ndcg = music_ndcg / len(rec_playlists)
        tag_ndcg = tag_ndcg / len(rec_playlists)
        score = music_ndcg * 0.85 + tag_ndcg * 0.15

        return music_ndcg, tag_ndcg, score

    def evaluate_with_save(self, gt_fname, rec_fname, model_file_path, default_file_path):
        # try:
        music_ndcg, tag_ndcg, score = self._eval(gt_fname, rec_fname)
        with open(f'{default_file_path}/results.txt','a') as f:
            f.write(model_file_path)
            f.write(f"\nMusic nDCG: {music_ndcg:.6}\n")
            f.write(f"Tag nDCG: {tag_ndcg:.6}\n")
            f.write(f"Score: {score:.6}\n\n")
            print(f"Music nDCG: {music_ndcg:.6}")
            print(f"Tag nDCG: {tag_ndcg:.6}")
            print(f"Score: {score:.6}")
        # except Exception as e:
        #     print(e)

    def evaluate(self, gt_fname, rec_fname):
        # try:
        music_ndcg, tag_ndcg, score = self._eval(gt_fname, rec_fname)
        print(f"Music nDCG: {music_ndcg:.6}")
        print(f"Tag nDCG: {tag_ndcg:.6}")
        print(f"Score: {score:.6}")