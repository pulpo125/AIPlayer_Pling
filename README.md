<img width="1178" alt="header" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/e7903c94-44e7-4384-806c-07b3c7edb0fb">

<br>

## 목차
[1) 프로젝트 개요](#프로젝트-개요) <br>
[2) 팀 구성](#팀-구성-(총-5명)) <br>
[3) 프로젝트 일정](#프로젝트-일정) <br>
[4) 개발 기술 스택](#개발-기술-스택) <br>
[5) 프로젝트 과정 및 내용](#프로젝트-과정-및-내용) <br>
[6) 웹 서비스](#웹-서비스) <br>

<br>

# 프로젝트 개요
AI Player는 플레이리스트 콘텐츠 크리에이터들을 위한 플레이리스트 자동 생성 서비스로, 사용자가 입력한 제목에 알맞은 플레이리스트 추천과 어울리는 썸네일 이미지를 자동으로 생성하는 서비스입니다.

<br>

# 팀 구성 (총 5명)
팀 **Pling**은 각각 데이터 분석 및 모델링을 담당하고 서비스 개발은 크게 프론트엔드, 백엔드, DB로 나누어 담당하여 협업을 진행했습니다.

### 강하영: 팀장, 모델링 및 서비스 개발 총괄
[브랜치] [hy_modeling](https://github.com/pulpo125/AIPlayer_Pling/tree/hy_modeling), [hy_web](https://github.com/pulpo125/AIPlayer_Pling/tree/hy_web)
 
### 김영지: 데이터 분석/DB 및 프론트엔드
[브랜치] [yj](https://github.com/pulpo125/AIPlayer_Pling/tree/yj), [youngji](https://github.com/pulpo125/AIPlayer_Pling/tree/youngji)

### 노예진: 이미지 생성 및 프론트엔드
[브랜치] [yejin](https://github.com/pulpo125/AIPlayer_Pling/tree/yejin)

###  유성재: 추천 알고리즘 및 백엔드
[브랜치] [jay](https://github.com/pulpo125/AIPlayer_Pling/tree/jay)

### 윤미루: 자연어 처리 및 DB/AWS
[브랜치] [miro](https://github.com/pulpo125/AIPlayer_Pling/tree/miro)

<br>

# 프로젝트 일정
- 9월 4일 ~ 10월 19일 (약 6 주간)

<img width="1178" alt="프로젝트 일정표" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/6f57707f-6b2d-4791-9c9e-4a1fcfcfa54c">

<br>

# 개발 기술 스택
<div align=center>
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  <br>
  <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white"> 
  <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"> 
  <br>
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> 
  <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> 
  <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"> 
  <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> 
  <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> 
  <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> 
  <img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=black"> 
  <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> 
  <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">
  <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> 
</div>

<br>

# 프로젝트 과정 및 내용
## 1. 데이터 준비
**[폴더] 1_analysis**
1. 데이터 수집
- 카카오 아레나에서 제공한 멜론 DJ 플레이리스트 데이터셋을 수집했습니다. 이 데이터셋은 멜론의 인증을 거친 DJ들의 플레이리스트로 신뢰도가 높습니다.

<br>

<img width="1178" alt="데이터셋구조" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/486a0b11-13da-4f86-897f-85cfafc1102b">

<br>

- 플레이리스트 데이터셋은 제목, 곡 리스트, 해시태그 리스트로 구성되어 있습니다. 저희 서비스 역시 플레이리스트의 곡과 태그를 추천해야 하기 때문에 인풋값을 축소하고 복원하는 과정에서 이 인풋값에 대한 중요한 특징을 학습하는 오토인코더를 활용하여 플레이리스트를 넣어 비슷하지만 또 다른 플레이리스트를 생성하는 추천 알고리즘을 구현하기로 결정했습니다.
이러한 추천 알고리즘은 사용자 로그 없는 협업 필터링이라는 큰 장점이 있습니다.

## 2. EDA 및 전처리
<img width="1178" alt="데이터전처리과정" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/5b575dc7-8efd-421c-b544-6c5fbff14426">

<br>

- EDA를 통해 알게된 결측치 및 이상치를 제거하고 추천 알고리즘인 오토인코더 학습을 위해 곡과 태그에 대한 Feature를 선별하는 작업을 진행했습니다. 오토인코더 학습을 위해서는 곡과 태그의 포함 여부에 대한 원-핫 인코딩을 해야 하는 데 저희 데이터셋의 고유 곡과 태그가 약 60만 개 이상으로 컴퓨팅 자원 제한 문제가 발생했습니다. 때문에, 빈도 수를 기준으로 상위 20%의 곡과 태그만을 Feature로 사용했습니다.

## 2. 모델링
### 1. 자연어 처리
**[폴더] 2_sBert**
- 플레이리스트 제목은 해당 플레이리스트를 구성하는 곡과 태그에 전체적인 분위기를 담고 있습니다. 때문에, 사용자가 플레이리스트 제목을 입력하면 sBert를 사용하여 변환한 임베딩을 저희 멜론 플레이리스트 제목 임베딩 데이터와 비교하여 코사인 유사도가 높은 Top 3를 사용자들에게 제공합니다. 이 중 사용자가 원하는 플레이리스트를 선택하게 되고 선택된 플레이리스트를 오토인코더의 인풋값으로 주어 추천을 진행하게 됩니다.
- 플레이리스트 제목이 전체적인 분위기를 담고 있다는 데이터의 특징을 활용하여 자연어 처리를 통한 추천 알고리즘의 인풋값을 선정하는 아이디어를 생각했습니다.

### 2. 추천 알고리즘
**[폴더] 3_autoEncoder**
<br>

<img width="1178" alt="추천과정" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/9c604725-0966-4160-b087-5bf1a68826b7">

- 카카오 아레나에서 제공한 nDCG 라는 평가지표를 사용하여 모델 평가를 진행했습니다. nDCG는 추천 결과의 구성 요소와 순서를 모두 고려하는 평가 지표 입니다. 때문에, 오토인코더의 아웃풋에서 확률이 높은 순으로 정렬하여 추천 결과를 생성합니다. 

### 3. 이미지 생성 모델
**[폴더] 4_imgModel**
- 플레이리스트 분위기와 유사한 이미지를 생성하기 위해 튜닝을 진행해야 하기 때문에 오픈 소스로 제공되는 Stable Diffusion을 사용했습니다. Stable Diffusion은 영어로 학습된 모델이므로 한국어로 입력된 플레이리스트 제목을 영어로 변환하기 위해 googletrans 라는 구글 번역기 라이브러리를 사용했습니다. 이렇게 영어로 번역된 제목은 Stable Diffusion의 프롬프트로 사용되게 됩니다.

- 썸네일 이미지는 풍경 사진이라는 특징이 있습니다. 때문에, 프롬프트 엔지니어링을 진행하여 풍경 사진과 같은 이미지를 생성하는 것에 집중했습니다. 
<img width="1182" alt="이미지" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/5617f64d-ecb3-48e4-a143-df331752b8a1">

## 3. 서비스 구현
### 1. DB 구축
**[폴더] 5_db**
![ERD](https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/a1447de6-f855-4d54-bbcc-bdbf4669788b)

- 데이터 플로우에 따른 효율적인 DB를 구성하기 위한 ERD 설계를 진행했습니다. 플레이리스트 데이터셋의 경우 곡id 리스트로 구성되어있기 때문에 이 곡에 대한 정보를 song_meta 테이블에서 검색해야 합니다. 그러므로, 이 둘의 관계를 나타내는 song_in_ply 테이블을 만들어 ply_meta와 song_meta를 연결하였습니다. 이러한 구조로 MySQL를 사용하여 DB를 구축했습니다.
- 새로운 플레이리스트 생성이 완료되고 사용자가 플레이리스트를 만족하여 좋아요 버튼을 누르게 되면 이 플레이리스트 데이터는 해당 DB로 저장되어 오토인코더 재학습에 사용하게 됩니다. 이를 통해, 더 고도화된 추천 알고리즘을 기대할 수 있습니다.

### 2. 장고 웹 프로젝트
**[폴더] 6_web**

<img width="1154" alt="시스템설계도" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/16f47901-75a7-40a8-a095-d07155d77f8b">

- 모든 모델 학습과 함수 파일은 파이썬으로 개발되었습니다. 때문에, 파이썬 웹프레임워크인 장고를 사용하여 웹을 구축했습니다. 이는 AI Server와 Web Server를 따로 구축할 필요가 없어 비용적으로 효율이 있습니다.   

<br>

- 서비스 배포 과정
<img width="1181" alt="배포과정" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/1ec7c4a2-c006-48b6-9510-815674bb79e2">

<br>

# 웹 서비스
![main](https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/8096185f-4058-4f82-be0c-e5e1316d5ee2)
![input](https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/44abfc64-0e6e-4f9d-b9fc-7457f296cb4b)
![loading](https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/b01101c7-8f9b-493c-adb8-70573acc84ab)
![output](https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/56c5431d-817a-4a80-8e9d-117e5768da64)  
