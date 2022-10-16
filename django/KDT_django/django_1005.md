# Django CRUD 코드 이해

> 깃 허브 순서에서 커밋 단위로 흐름 정리 해보기

우리는 결국 웹프레임워크 장고를 학습하고 있다.

프레임워크란 틀에 박힌 일. 

````
1. URL로 요청을 받아서 
2. 처리하고 
3. 응답을 한다.
````

정적 사이트와 다른 점은 DB에서 값을 가지고 오고, 저장하는 로직을 가지고 있고, 이를 도와주는 것이 `DJANGO orm`

처리하고 응답을 하는 것 = views의 역할

응답을 html을 만들어서 보여주는 것 = Templates의 역할

서비스 기능을 만들기 위해 기능을 구성



- 게시판을 구현할 때의 로직

  > 가장 먼저 해야할 일은 요청받는 URL

  - 글을 생성 : `/articles/new/`(Form 을 제공), `articles/create/`(DB에 저장)

    생성을 하기 위해서는 브라우저에 `Form`을 제공해주어야 한다.(html에)

    받은 폼을 DB에 저장하는 과정이 필요

  - 조회하고 : `articles/detail/` 

    글을 누르면 DB의 `<특정>`variaable routing  값을 조회하도록

  - 삭제하고 : `articles/delete/` 

    버튼을 누르면 `<특정>` DB값 삭제하도록

  - 수정하고 

    HTML From + 기존 값

    DB 저장 과정

    

- URL 요청(HTTP 요청 메시지)

  > 클라이언트는 결국 http 메시지로 요청할 수밖에 없다.

  **HTTP 요청 메시지 4가지**

  **<u>path</u>**/**<u>메서드</u>**/헤더/프로토콜



- 장고는 생성과 수정을 도와주고 싶었다 -> `ModelForm`

  DB필드가 사실상 HTML Form 과 연관이 있다.

  Input 값이 항상 DB에 들어가기 전에 유효성 검사



- 모델폼에서 중요한 것

  어떤 모델(Model)에서 어떤 필드(Fields)를 받아올 것인가



- 사용하는 ORM

  - GET일 때 Article.objects.create()

  - Article.objects.get()

  - Article.obejects.delete()

  - Article.objects.get()해서 가져와서 수정 후 save()



# 첫 번째 쉬는시간

django : 파이썬 기반 웹 프레임워크

가상환경을 사용하는 이유

> 가상환경 : 프로젝트별 별도 패키지 관리

Django : 주요 기능 단위의 App 구조, App 별로 MTV의 구조를 가지는 모습 + 'urls.py'

1. 앱 생성

   ```
   python manage.py startapp `app_name`
   ```

2. 앱 등록

   ```
   `settings.py` 파일의 `INSTALLED_APPS`에 추가
   ```

3. urls.py 설정

   ```
   # 프로젝트/urls.py
   
   urlpatterns = [
   ...
   path('articles/', include('articles.urls')),
   						모듈:앱 이름.urls
   						=> articles/urls.py
   ]
   ```

   

- HTML Form 태그 활용 시 핵심
  - 어떤 필드를 구성할 것인지(`name`, `value`)
  - 어디로 보낼 것인지 (`action`, `method`)



GET 방식으로 요청했을 때 url의 쿼리 string에서 등장하는 title과 content는 어디로부터 왔는가?

=> input 태그의 name에서!



custom validation





Static Files

웹 서버는 요청받은 url로 서버에 존재하는 정적 자원을 제공

url 에서 상대경로를 어떻게 가지는가?



# static filews

articles의 내부에 있지만