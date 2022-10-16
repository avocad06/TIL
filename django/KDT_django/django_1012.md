왜 `auth.User`를 사용하지 않는 건가요?

기본 User모델이 Abstract를 상속받고 있으니까 우리가 만드는 Custom도 Abstract를 상속시키자



.save()

return user라는 객체를 돌려받는다.

User모델이라는 건 결국 변경이 가능한 친구이면서 django + 사용자가 쓰는 것

결국에는 변경가능한 것은 어찌 되었든 변수화 등을 통해서 예를 호출하도록 하는 것이 좋다

범개발 영역에서의 핵심 관통



HTTP의 특징

- 서버는 요청에 대한 응답을 보낸 후 연결을 끊는다.
- 상태라는 게 없다. 연결을 끊는 순간 상태 정보가 유지되지 않는다.
- 그러면 어떻게 로그인 상태를 유지하고 있는 거야?
  - 서버와 클라이언트 간 지속적인 상태 유지를 위해 "쿠키와 세션"이 존재한다.
  - 실시간 라이브는? => 웹 소켓이라는 프로토콜을 활용
- 쿠키 : 사용자의 브라우저에 설치되는 작은 기록 정보 파일
- HTTP에서 상태 정보를 관리



쿠키 사용 예시

- 서버에 응답을 요청할 때마다 생성?

- 쿠키는 수명이 존재



- 미들웨어?

  앱은 동작하게 도와주는 것

  미들웨어는 요청이 들어오면 미들웨어 순으로 처리해야할 것을 관리한다.

  응답을 하면 미들웨어 역순으로

  절차를 관리하는 변수



로그인 기능

- 1단(First) URL



AuthenticationForm을 활용하지 않고 로직을 다 짜겠다고 하면,





# 오후실습

1. 가상환경 생성

   ```bash
   $ python -m venv venv
   ```

2. 가상환경 실행

   ```
   $ . venv/Scripts/activate
   ```

3. 가상환경에 django 설치

    ```bash
    $ pip install django==3.2.13
    ```

4. django 프로젝트 생성(시작)<br>📌 `.`주의하기 : 현재 폴더를 프로젝트 폴더로 지정한다.

   ```bash
   $ django-admin startproject mysite .
   ```

5. vs code열고, app 생성<br>📌 가상환경이 실행되고 있는지 확인(`(venv)`)

   📌 `ls`로 현재 폴더에 `manage.py`가 있는 지 확인

   ```bash
   $ code .
   ```

   ```bash
   (venv) 
   user@DESKTOP-G5JHA23 MINGW64 /d/djngo_practice/day11
   
   $ ls
   accounts/  manage.py*  mysite/  venv/
   ```

   ```bash
   $ python manage.py startapp accounts
   ```

6. app을 생성했으면 등록(`mysite` > `settings.py`)

   ```python
   INSTALLED_APPS = [
       'accounts', # 추가
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

7. `settings.py`들어온 김에 

   1. `base.html` 템플릿 상속을 위해 `BASE_DIR`추가
   2. 한국어 지원을 위해 `ko-kr` , `Asia/Seoul` 추가

   ```python
   LANGUAGE_CODE = 'ko-kr'
   
   TIME_ZONE = 'Asia/Seoul'
   
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR / 'templates'],
   ```

8. 서버 돌려서 한국어 출력 잘 되는지 확인해보기

   ```bash
   $ python manage.py runserver
   ```

9. 템플릿 상속을 위해 `base.html` 추가(`DAY11` > `templates` > `base.html`)<br>

   `base.html`에 `{% block ___ %}` `{% endblock %}` 추가하기

   📌 보통은 `<body>` 태그 사이에 추가한다.

   ```html
     <body>
       {% block forms%}
       {% endblock %}
     </body>
   ```

10. 앱 구현(기능의 추가)의 첫 단계는 `url` 생성 (`프로젝트 폴더` > `urls.py`)

    📌 프로젝트 단위의 url에서 app 단위 url이 요청으로 들어오면 app.urls에서 처리한다.

    ```python
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path("", include("accounts.urls")),
    ]
    ```

11. app 폴더에 `urls.py`를 추가한다.(`app 폴더` > `urls.py`)

    요청이 들어온 url을 처리할 `urlpatterns`를 작성한다.

    ```python
    from django.urls import path
    
    app_name = "accounts"
    
    urlpatterns = [
        
    ]
    ```

12. 요청 url 주소를 작성한다.(`views.함수` : 요청이 들어오면 어떤 처리를 해서 응답할 것인지 결정)

    ```python
    from . import views 
    
    urlpatterns = [
        # 회원가입 페이지
        path("accounts/signup/", views.signup, name="signup"),
        # 회원목록 조회
        path("accounts/", views.index, name="index"),
        # 회원 정보 조회
        path("accounts/<user_pk>", views.detail, name="detail"),
        # 로그인 페이지
        path("accounts/login/", views.login, name="login"),
        # 로그아웃
        path("acocunts/logout/", views.logout, name="logtout"),
    ]
    ```

13. `urls.py`에서 정한 함수의 기능과 명세에 따라 view함수를 정의한다.(`app 폴더` > `views.py` )

    ```python
    def signup(request):
        return render(request, "accounts/signup.html")
    ```

14. `views.py`에서 응답하기로 한 템플릿을 생성하고, (`app폴더` > `templates` > `app 폴더` > `___.html` )

    1. `base.html`에서 템플릿 상속을 잘 받고 있는지,

    2. `urls.py`에서 오류나는 함수는 없는지 확인을 위해 서버를 돌려본다.

    ```html
    {% extends 'base.html' %}
    {% block forms %}
      <h1>출력되는지 확인합니다.</h1>
    {% endblock %}
    ```

    ```bash
    $ python manage.py runserver
    ```

15. 정상 작동되는지 확인했으면, DB생성을 위해 `model`을 정의한다.(`app 폴더` > `models.py`)

    15-1. User모델을 정의할 때는, `django.contrib.auth.models` 의 모델 클래스 상속을 통해 User모델을 커스텀해야 한다.

    📌 User모델 커스터마이징은 **첫 번째** 마이그레이션 이전에 진행해야 한다.   
    
    ```python
	from django.db import models
    from django.contrib.auth.models import AbstractUser
    # Create your models here.
    
    # 기본 User모델이 AbstractUser를 상속받고 있으므로
    class User(AbstractUser):
        pass
	```
	
	15-2. User모델을 새로 정의했으면, `AUTH_USER_MODELS` 의 값도 변경을 해준다.(`프로젝트 폴더`> `settings.py`)
	
	```python
	AUTH_USER_MODEL = 'accounts.User'
	```
	
16. 모델을 정의했으면 마이그레이션을 해준다.

    📌 User테이블이 커스텀 유저 모델로 되어있음을 확인(`app이름_모델이름`)

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

    ```
    accounts_user
    ```

    17. 모델을 DB에 반영하였으므로 `views.함수`를 기능과 명세에 따라 재정의한다.(`app 폴더` > `views.py`)

        17-1. `signup`함수의 역할은 회원가입 폼을 제공하는 것이다. 로그인폼은 `django.contrib.auth.forms` 의 `UserCreationForm`을 사용한다.

        17-2. 하지만 `django.contrib.auth.forms` 가 제공하고 있는 `UserCreationForm`은 `ModelForm`을 상속받고 있는데, 그 안에서 정해진 `model`속성이 커스텀된 User모델이 아닌 기본 User모델이다.

        17-3. 결국 User모델을 커스터마이징했던 것처럼, 회원가입폼도 클래스를 상속받아 커스터마이징(재정의)을 해주어야 한다.

        17-4. `UserCreationForm`은 `MdoelForm`을 상속받고 있으므로 `model`속성에 커스텀된 User모델을 넣어야 한다.

        📌 User모델을 가져올 때는 `django.contrib.auth` 의 `get_user_model`로 경로를 가져오는 것이 좋다. (변화 가능한 요소에 대해서는 변수화)

        ```python
        # from .models import User
        from django.contrib.auth import get_user_model
        ```

        17-5. `UserCreationForm`모델을 상속받을 것이므로 가져와서 상속한다.(ModelForm을 생성했을 때와 같다.)

        ```python
        from django.contrib.auth.forms import UserCreationForm
        
        class SignUpForm(UserCreationForm):
            
            class Meta:
                model = get_user_model()
                # 함수를 호출하여 커스텀된 User모델을 가져온다.
        ```

        17-6. Form의 `fields`속성은 명세에 따라 정의한다.

        ```python
        from django.contrib.auth import get_user_model
        from django.contrib.auth.forms import UserCreationForm
        
        class SignUpForm(UserCreationForm):
            
            class Meta:
                model = get_user_model()
                fields = ("username", "email")
        ```

        17-7. `views.py`로 돌아가서 `signup`함수를 정의한다.(`app 폴더` > `views.py`) <br>가져오는 회원가입폼이 달라졌으므로 커스터마이징된 `UserCreationForm`을 가져온다.

        ```python
        from .forms import SignUpForm
        ```

        17-8. `signup`함수를 정의한다.(`GET`일 때는 빈 폼을, `POST`일 때는 DB에 저장하는 로직)
        
         📌 회원가입 완료 후의 처리는 <u>기획의 영역</u>이다. (`redirect`, `render` 등)
        
        ```python
        def signup(request):
            # 리퀘스트 메소드가 post일 땐
            # DB에 저장한다
            if request.method == "POST":
                forms = SignupForm(request.POST)
                # 유효성 검사 진행 후 DB에 저장
                if forms.is_valid():
                    forms.save()
                    return render(request, "base.html")
            
            # 리퀘스트 메서드가 get 또는 유효성 검사를 통과하지 못했다면,
            else:
                # 빈 폼 또는 폼의 오류메시지
                forms = SignupForm()
            
            context = {
                "forms" : forms,
            }
            return render(request, "accounts/signup.html", context)
        ```
        
        17-9. views함수를 정의했으므로 사용자의 입력값을 받아올 html을 생성한다.
        
        ```html
        {% extends 'base.html' %}
        {% load django_bootstrap5 %}
        {% block content %}
          <div class="w-50 container border border-secondary rounded-3 p-5">
            <div class="h4 pb-2 mb-4 text-black fw-bold border-bottom border-secondary">
              함께 해 주세요
            </div>
            <form action="" method="POST" class="fw-bold">
              {% csrf_token %}
              {% bootstrap_form forms %}
              <div class="text-end d-grid">
                <input type="submit" class="btn btn-outline-primary" value="가입하기">
              </div>
            </form>
          </div>
        {% endblock %}
        ```
        
        
