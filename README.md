<img width="1000" alt="header" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/e7903c94-44e7-4384-806c-07b3c7edb0fb">

<br>

## 📌 목차
[1) 프로젝트 개요](#프로젝트-개요) <br>
[2) 프로젝트 내용](#프로젝트-내용) <br>
[3) 프로젝트 과정](#프로젝트-과정) <br>
[4) 프로젝트 결과](#프로젝트-결과) <br>

<br>

# 프로젝트 개요
<img width="1000" alt="AI Player UI" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/f2d2bbc8-a012-4bdb-9314-176121267061">

> **AI Player**는 플레이리스트 콘텐츠 크리에이터들을 위한 플레이리스트 자동 생성 서비스로, 사용자가 입력한 제목에 알맞은 `플레이리스트 추천`과 어울리는 `썸네일 이미지`를 자동으로 생성하는 서비스입니다.

<br>

## 📆 프로젝트 일정
- 9월 4일 ~ 10월 19일 (약 6 주간)

<img width="1000" alt="프로젝트 일정표" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/6f57707f-6b2d-4791-9c9e-4a1fcfcfa54c">

<br>

## 🧑‍🤝‍🧑 팀 구성 (총 5명)
팀 **Pling**은 각각 데이터 분석 및 모델링을 담당하고 서비스 개발은 크게 프론트엔드, 백엔드, DB로 나누어 담당하여 협업을 진행했습니다.

|구분|성명|역할|브랜치|
|---|---|---|---|
|팀장|강하영|추천 알고리즘 및 이미지 생성 모델 개발, 백엔드|[hy_modeling](https://github.com/pulpo125/AIPlayer_Pling/tree/hy_modeling), [hy_web](https://github.com/pulpo125/AIPlayer_Pling/tree/hy_web)|
|팀원|김영지|데이터 분석, UI/UX 디자인 및 프론트엔드|[yj](https://github.com/pulpo125/AIPlayer_Pling/tree/yj), [youngji](https://github.com/pulpo125/AIPlayer_Pling/tree/youngji)|
|팀원|노예진|이미지 생성 모델 개발, UX/UI 디자인 및 프론트엔드|[yejin](https://github.com/pulpo125/AIPlayer_Pling/tree/yejin)|
|팀원|유성재|추천 알고리즘 개발|[jay](https://github.com/pulpo125/AIPlayer_Pling/tree/jay)|
|팀원|윤미루|자연어 처리 모델 개발, 데이터베이스 및 시스템 환경 구축|[miro](https://github.com/pulpo125/AIPlayer_Pling/tree/miro)|


<br>

## 🔨 개발 기술 스택
|Stack|사용목적|
|:---:|:---:|
|<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">|프로그래밍 언어|
|<img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white"> <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white">|통합 개발 환경 / 이미지 생성 연구 환경|
|<img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"> <img src="https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white">|딥러닝|
|<img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> |데이터베이스|
|<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">|백엔드|
|<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"> <br> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">|프론트엔드|
|<img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white"> |UX/UI 설계|
|<img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white"> <img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=black"> |클라우드/웹서버/OS|
|<img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">|프로젝트&형상 관리|

<br>

# 프로젝트 내용
### 주요 기능
1. 유사한 플레이리스트 조회 및 선택
    ```
    ✔️ 'SBERT'를 사용하여 사용자가 입력한 타이틀과 유사한 플레이리스트 'Top 3'를 제공
    ✔️ 사용자가 선택한 유사한 플레이리스트는 플레이리스트 추천에 활용
    ```
2. 플레이리스트 추천
    ```
    ✔️ 'AutoEncoder'를 사용하여 곡과 해시태그로 구성된 플레이리스트 추천
    ✔️ 사용자가 원하는 유사한 플레이리스트의 조합으로 선택할 수 있어 다양한 추천 결과 제공 가능
    ```
3. 썸네일 이미지 생성
    ```
    ✔️ 'Stable Diffusion'을 사용하여 사용자가 입력한 타이틀에 부합하는 썸네일 이미지 생성
    ```
### 세부 기능
1. 유사도 및 곡 개수 커스터마이징
    ```
    ✔️ '유사도': 슬라이드 바를 통해 선택 플레이리스트와 추천 플레이리스트의 유사도 조정
    ✔️ '곡 개수': 슬라이드 바를 통해 추천 플레이리스트의 곡 개수 조정
    ```
2. 피드백
    ```
    ✔️ '좋아요' 버튼 클릭 시 해당 추천 결과가 DB에 저장되어 모델 재학습에 사용
    ```
3. 이미지 다운로드
    ```
    ✔️ '이미지 다운로드' 버튼 클릭 시 유튜브 썸네일 규격에 맞는 사이즈의 이미지 제공
    ```
4. SNS 공유
    ```
    ✔️ 'SNS 공유' 버튼 클릭 시 전체 결과 화면 캡처를 주요 SNS 플랫폼에 공유
    ```

<br>

# 프로젝트 과정
[<img src="https://img.shields.io/badge/Click Me-000000?style=flat-square&logo=github&logoColor=white"/>](https://github.com/pulpo125/AIPlayer_Pling/blob/main/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EA%B3%BC%EC%A0%95.md) ▶️ 상세한 프로젝트 과정이 궁금하다면 방문해주세요.

<br>

# 프로젝트 결과
<div align=center>
  <img width="1000" alt="main" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/8096185f-4058-4f82-be0c-e5e1316d5ee2">
  <img width="1000" alt="input" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/44abfc64-0e6e-4f9d-b9fc-7457f296cb4b">
  <img width="1000" alt="loading" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/b01101c7-8f9b-493c-adb8-70573acc84ab">
  <img width="1000" alt="output" src="https://github.com/pulpo125/AIPlayer_Pling/assets/118874524/56c5431d-817a-4a80-8e9d-117e5768da64">
</div>
