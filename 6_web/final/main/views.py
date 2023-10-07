from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from main.ai.autoencoder import ply_to_onehot, recommendation, apply_sim
from main.models import PlyMeta, SongMeta, SongInPly, PlyTitleEmbedding, UserLog
from main.ai.bert import encoding, get_sim_ply_id, emd_to_array
import pandas as pd
import ast

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
        sim_ply_id = get_sim_ply_id(ply_title_embedding, new_embedding, n=3)
        
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
        # Insert: UserLog
        str_embedding = ', '.join(map(str, new_embedding))
        new_user = UserLog(user_title = new_title,  user_title_embedding = str_embedding, user_updt = timezone.now())
        new_user.save()

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
        
        similarity = int(similarity)
        song_num = int(song_num)

        input_song, input_tag, input_onehot = ply_to_onehot(select_ply_lst)
        print('onehot')
        rec_song, rec_tag = recommendation(input_song, input_tag, input_onehot, song_num, tag_num=5, song_len=88146)
        print('recommend')
        # # 유사도 적용
        sim_reco_song  = apply_sim(similarity, input_song, rec_song, song_num)
        print('유사도')
    # DB 저장
    str_tag = ', '.join(rec_tag)
    user_id = UserLog.objects.last().user_id
    UserLog.objects.filter(user_id=user_id).update(user_song_id_lst = sim_reco_song, user_tag_lst = str_tag)
    print('DB저장')
    return render(request, '3_loading.html')


def output(request):

    # 추천 결과 가져오기
    user_meta = UserLog.objects.last()
    user_title = user_meta.user_title
    user_song_id_lst = user_meta.user_song_id_lst
    user_tag_lst = user_meta.user_tag_lst

    # str -> list로 변환
    rec_song_lst = ast.literal_eval(user_song_id_lst)
    rec_tag_lst = user_tag_lst.split(',')

    # song_id 별 song_name. artist_name_lst
    rec_song_meta = []
    for rec_song_id in rec_song_lst:
        queryset = SongMeta.objects.filter(song_id=rec_song_id).values('song_name', 'artist_name_lst')
        rec_song_meta.append({'song':queryset[0]['song_name'], 'artist':queryset[0]['artist_name_lst']})
    
    context = {'user_title':user_title, 'rec_song_meta': rec_song_meta, 'rec_tag': rec_tag_lst}

    return render(request, '4_output.html', context=context)

def like_ply(request):
    if request.method == 'GET':
        # 좋아요 버튼이 클릭된 경우
        user_id = UserLog.objects.last().user_id
        if user_id:
            UserLog.objects.filter(user_id=user_id).update(user_like_cnt = 1)
            success_value = True
    else:
        success_value = False

    return JsonResponse({"success": success_value})