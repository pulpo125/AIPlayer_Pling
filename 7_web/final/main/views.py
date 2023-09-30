from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from main.models import PlyMeta, SongMeta, SongInPly, PlyTitleEmbedding
# from main.ai.bert import encoding, get_sim_ply_id, emd_to_array
# from main.ai.autoencoder import make_features, ply_to_onehot, recommendation
import pandas as pd

def index(request):
    return render(request, "1_index.html")

def input(request):
    return render(request, "2_input.html")

# def similar_ply(request):
#     try:
#         new_title = request.GET.get('new_title')

#         # 입력받은 타이틀을 임베딩으로 변환
#         new_embedding = encoding(new_title)

#         # 가장 유사한 플레이리스트 id list 추출
#         ply_title_embedding = pd.DataFrame(list(PlyTitleEmbedding.objects.all().values()))
#         ply_title_embedding['ply_title_emd'] = emd_to_array(ply_title_embedding)
#         sim_ply_id = get_sim_ply_id(ply_title_embedding, new_embedding, n=2)
        
#         # 유사 플리 정보 조회
#         sim_ply_info = []
#         for id in sim_ply_id:
#             id_info = []
#             queryset = (PlyMeta.objects.filter(ply_id=id).filter(plyto__song__isnull=False).values('ply_id', 'ply_title', 'plyto__song__song_name', 'plyto__song__artist_name_lst'))
#             id_info.extend(queryset)
#             song_meta = []
#             for info in id_info:
#                 song_meta.append({'song_name': info['plyto__song__song_name'], 'artist_name': info['plyto__song__artist_name_lst']})
#             sim_ply_info.append({'ply_id': id, 'ply_title': id_info[0]['ply_title'], 'song_meta': song_meta})

#         # DB 저장
#         # Insert: 새로운 플리 제목 -> 수정 user db에 저장
#         # new_ply_id = PlyMeta.objects.last().ply_id + 1 # 새로운 플리 id = 플리 id 마지막 값 + 1
#         # new_ply = PlyMeta(ply_id = new_ply_id, ply_title = new_title, ply_updt = timezone.now())
#         # new_ply.save()

#         # Insert: 새로운 플리 타이틀 임베딩
#         # insert_emd = PlyTitleEmbedding(ply_id = new_ply_id, ply_title_emd = new_embedding)
#         # insert_emd.save()

#         return JsonResponse({"sim_ply_info": sim_ply_info})

#     except Exception as e:
#         # 예외가 발생한 경우 오류 응답을 반환합니다.
#         return JsonResponse({"error": str(e)}, status=500)

# def loading(request):
#     pl_id, song_num, tag_num = 122388, 20, 10
#     features, song_len = make_features(song_num, tag_num)
#     onehot = ply_to_onehot(pl_id, features)
#     # model = 'C:/mockup/final/main/ai/autoencoder_denoise_ad.h5' # py 파일로 이동
#     p_song, p_tag = recommendation(onehot, features, song_len, song_num, tag_num)
    
#     p_song, p_tag = p_song[:5], p_tag[:5] # test로 5개만 뽑아봄

#     # song_id 별 song_name. artist_name_lst
#     song_meta = []
#     for p_song_id in p_song:
#         queryset = SongMeta.objects.filter(song_id=p_song_id).values('song_name', 'artist_name_lst')
#         song_meta.append({'song':queryset[0]['song_name'], 'artist':queryset[0]['artist_name_lst']})

#     return render(request, '3_loading.html', context={'song_meta': song_meta, 'p_tag': p_tag})

# def output(request):
#     return render(request, "4_output.html")