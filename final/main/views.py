from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from main.models import PlyMeta, SongMeta, SongInPly, PlyTitleEmbedding
from main.ai.bert import encoding, get_sim_ply_id, emd_to_array
import pandas as pd
from django.http import HttpResponse
from django.conf import settings
import os

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
    return render(request, "3_loading.html")

def output(request):
    return render(request, "4_output.html")


# test 화면
def input_title(request):
    return render(request, 'input_title.html')

def custom(request):
    if request.method == 'POST':

        new_title = request.POST['new_title']

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

        return render(request, 'custom.html', context={'sim_ply_info': sim_ply_info})
    

def download_image(request): # 이미지 다운로드
    # 이미지 파일의 경로 설정 (static/result 폴더 내의 이미지)
    image_path = os.path.join(settings.STATIC_ROOT, 'result', 'your_image.jpg')  # 이미지 파일 경로를 적절하게 변경하세요

    # 이미지 파일을 읽어 HTTP 응답으로 반환
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            response = HttpResponse(image_file.read(), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename="pubao.jpg"'  # 다운로드할 파일 이름 설정
            return response
    else:
        # 이미지 파일이 없는 경우 404 응답 반환
        return HttpResponse("이미지를 찾을 수 없습니다.", status=404)
    

def input_slider(request):
    return render(request, "2_input_slider.html")