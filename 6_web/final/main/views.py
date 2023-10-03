from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from main.ai.autoencoder import ply_to_onehot, recommendation, apply_sim
from main.models import PlyMeta, SongMeta, SongInPly, PlyTitleEmbedding
from main.ai.bert import encoding, get_sim_ply_id, emd_to_array
import pandas as pd

def index(request):
    return render(request, "1_index.html")

def input(request):
    return render(request, "2_input.html")

def similar_ply(request):
    try:
        new_title = request.GET.get('new_title')

        # 입력받은 타이틀을 임베딩으로 변환
        new_embedding = encoding(new_title)

        # 가장 유사한 플레이리스트 id list 추출
        ply_title_embedding = pd.DataFrame(list(PlyTitleEmbedding.objects.all().values()))
        ply_title_embedding['ply_title_emd'] = emd_to_array(ply_title_embedding)
        sim_ply_id = get_sim_ply_id(ply_title_embedding, new_embedding, n=2)
        
        # 유사 플리 정보 조회
        sim_ply_info = []
        for id in sim_ply_id:
            id_info = []
            queryset = (PlyMeta.objects.filter(ply_id=id).filter(plyto__song__isnull=False).values('ply_id', 'ply_title', 'plyto__song__song_name', 'plyto__song__artist_name_lst'))
            id_info.extend(queryset)
            song_meta = []
            for info in id_info:
                song_meta.append({'song_name': info['plyto__song__song_name'], 'artist_name': info['plyto__song__artist_name_lst']})
            sim_ply_info.append({'ply_id': id, 'ply_title': id_info[0]['ply_title'], 'song_meta': song_meta})

        # DB 저장
        # Insert: 새로운 플리 제목 -> 수정 user db에 저장
        # new_ply_id = PlyMeta.objects.last().ply_id + 1 # 새로운 플리 id = 플리 id 마지막 값 + 1
        # new_ply = PlyMeta(ply_id = new_ply_id, ply_title = new_title, ply_updt = timezone.now())
        # new_ply.save()

        # Insert: 새로운 플리 타이틀 임베딩
        # insert_emd = PlyTitleEmbedding(ply_id = new_ply_id, ply_title_emd = new_embedding)
        # insert_emd.save()

        return JsonResponse({"sim_ply_info": sim_ply_info})

    except Exception as e:
        # 예외가 발생한 경우 오류 응답을 반환합니다.
        return JsonResponse({"error": str(e)}, status=500)


def loading(request):
    if request.method == 'POST':
        # POST 요청으로 전송된 데이터 받기
        select_ply_lst = request.POST.getlist('select_ply') 
        similarity = request.POST.get('similarity', '')  # 슬라이더의 값을 가져옴
        song_num = request.POST.get('song_num', '')      # 슬라이더의 값을 가져옴

        input_song, input_tag, input_onehot = ply_to_onehot(select_ply_lst)
        rec_song, rec_tag = recommendation(input_song, input_tag, input_onehot, song_num, tag_num=5, song_len=22798)

        # # 유사도 적용
        sim_reco_song  = apply_sim(similarity, input_song, rec_song, song_num)

        # song_id 별 song_name. artist_name_lst
        rec_song_meta = []
        for rec_song_id in sim_reco_song:
            queryset = SongMeta.objects.filter(song_id=rec_song_id).values('song_name', 'artist_name_lst')
            rec_song_meta.append({'song':queryset[0]['song_name'], 'artist':queryset[0]['artist_name_lst']})
    
    return render(request, '3_loading.html', context={'rec_song_meta': rec_song_meta, 'rec_tag': rec_tag})

def output(request):
    return render(request, "4_output.html")