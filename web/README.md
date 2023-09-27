- 가상 환경 생성
위치: final_project/web
$python -m venv env

- 가상 환경 활성화
$env\Scripts\activate.bat

- DB 연동 설정
mysite > settings.py
DATABASE 부분 변경

- DB 변경 적용
위치: final_project/web/final
$python manage.py makemigrations (처음 1회만 실행)
$python manage.py migrate

- 정적 파일 적용 (static 폴더 안 img, js, css 등)
$python manage.py collectstatic

- runserver
$python manage.py runserver

