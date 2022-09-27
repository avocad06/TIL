Object Relation Mapping

멀티앱

practices: ping pong 기능(form 활용 데이터 전송)

-> practices/urls.py

articles: 방명록(저장되는 기능)

-> articles/urls.py

# 멀티앱이 됐을 때 url을 설정하는 방법

왜 따로 설정해야 할까? 관심사의 분리

분리되지 않은 느낌, 확장성 있게 앱을 만드는데 필요

- views 가 중복(멀티앱이 되면 고려해야할 사항이 많다)

  from practices import views 

  from articles import views

path('', views.)

앱 안의 template 디렉토리가 아닌 프로젝트 상단의 templates 디렉토리 안에 위치하고 싶다면 어떻게 해야 할까?

settings.py > TEMPLATES > DIRS:['BASE_DIR']

공통폴더 안에 templates 폴더 하나를 더 생성

상대경로 : 앱으로부터 바로 떨어지는 

BASE_DIR : pathlib 어떤 OS에서든 특정한 파일을 기준으로 django의 절대경로를 가져오고 싶을 때 path

즉, 기본이 되는 파일, 프로그램 자체를 지칭하는 예약어

기본적으로 추구하는 convention 

핵심은 base.html 은 특정 앱 폴더가 아니라 앱의 최상단, 프로젝트 최상단 등 있을 곳을 지정해주어야 함.

=> 중립으로 빠져나와 있는 것이 중요하다.

templates 폴더를 최상단에 생성

DIRS: [BASE_DIR / 'templates',],

BASE_DIR 은 경로다.



- url 분리해서 관리하기

  > 유튜브 안의 유튜브 short, music, 등

  각각의 앱 안에 urls.py를 만들어주기(서브 문지기 만들어주기)

  from django.urls import path

  from . import views

  urlpatterns = [

  path(어쩌구)

  ]

- 그럼 메인 문지기는 뭘하나 ?

  오 include() 서브문지기를 찾으면 서브 문지기에게 보내기

- 방명록 만들기

  div

  h1 방명록

  /div

  div

  h2 글목록

  p 글1

  p 글2

  p 글..

  /div

  div

  h2 글 작성

  form action="/articles/create/"

  input type="text" name="content"

  input type-"submit"

  /form



- 



# 오전 실습 복습

패키지 설치 후

python manage.py shell_plus

=> 실습 준비 완



