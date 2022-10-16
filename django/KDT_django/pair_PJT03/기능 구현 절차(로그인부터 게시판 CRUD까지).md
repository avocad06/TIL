# 기능 구현 절차(로그인부터 게시판 CRUD까지)

## 로그인

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`accounts` > `urls.py`)

   📌 <u>**1**단 **url**이 먼저다</u>

   ```python
   path("login/", views.login, name="login"),
   ```

2. url을 추가했으면 `views`로 가서 `login`함수를 정의한다.(`accounts` > `views.py` )

   `login`함수는 request.method가 `GET`일 때는 빈 로그인 폼을 보여주는 템플릿을 출력하고, `POST`일 때는 유효성 검사 후 DB의 <u>세션에 저장한다.</u> 

   

   로그인 폼은 `django.atrib.auth.forms`의 `AuthenticationForm`을 활용한다.

   ```python
   from django.contrib.auth.forms import AuthenticationForm
   ```

   

   모델폼을 상속받는 회원가입 폼과 달리 일반 `form`을 상속받는 로그인 폼은 요구하는 매개변수가 다르고, 호출할 수 있는 메서드가 다르다. (상속 : 속성과 메서드를 상속 받는 것)

   모델폼의 값을 DB에 저장했던 메소드 <u>`.save()`를 사용할 수 없으므로</u> 유효성 검사를 통과한 사용자의 입력값(`request.POST`)을 DB 세션에 저장하는 내장함수 `login()`을 호출한다. `views`함수와 이름이 겹치므로 `as __`를 활용한다. ex) `as auth_login`

   ```python
   from django.contrib.auth import login as auth_login
   ```

   

   이후 로그인을 먼저 요구하는 페이지에 접속 했을 때, <u>로그인 이후 바로 요청한 페이지로 이동할 수 있도록</u> 경우를 분기한다.

   로그인은 로그인 url(`accounts/login`)에서 이루어진다.

   1. 로그인 성공 이후 넘어가는 페이지는 두 가지의 경우가 있다.

      1. 로그인 페이지에서 로그인을 성공했을 경우
      2. 로그인을 요구하는 페이지에 접속했을 때 로그인 이전 요청했던 페이지를 넘겨주는 경우

      `1-1`의 경우는 기획의 영역(로그인 성공 후 메인으로 넘겨줄지, 다른 페이지로 넘겨줄지)

      하지만 `1-2`의 경우는 사용자가 요청한 페이지로 넘겨주어야 하므로 요청 값을 저장하고 있어야 한다. 사용자는 `GET`방식으로 페이지를 요청하므로 요청 값은 URL의 쿼리 문자열 매개변수에 저장된다.

   2. `django.contrib.auth.decorators`의 데코레이터 `login_required`는 사용자가 요청한 url을 변경하지 않고,  `accounts/login/`(`settings.py` `LOGIN_URL`에 저장된 문자열 주소) 로 redirect한다.

      📌 사용자가 요청한 로그인을 요구하는 페이지의 url은 쿼리 문자열 매개변수 `next`에 담긴다. 

      ````
      http://localhost:8000/accounts/login/?next='사용자가 요청한 url'
      ````

      ```python
      # print(request.GET)
      <QueryDict: {'next': ['/reviews/create/']}>
      ```

   3. 사용자의 요청 값은 매개변수  `next`에 저장되어 있으므로, 로그인 이후 다음 페이지를 요청하는 경우 `next`의 키 값을 가져와서 해당 url로 redirect 하고, 값이 없다면 기획한 대로 url를 redirect 하면 된다.

      ```python
      def login(request):        
          # request method가 POST일 때
          if request.method == "POST":
              # 사용자의 입력값을 받는다.
              # 모델폼을 상속하는 폼이 아니기 때문에 요구하는 문법(매개변수)가 다르다.
              forms = AuthenticationForm(request, data=request.POST)
              # 유효성 검사를 통과하면 세션에 저장한다.(내장함수 login으로)
              if forms.is_valid():
                  auth_login(request, forms.get_user())
                  # 로그인이 요구되는 페이지를 접근하기 위해 로그인한 경우
                  # 로그인이 성공하면 해당 페이지로 넘겨준다
                  # 로그인 후 요청되는 페이지가 없다면 메인 페이지로 넘겨준다.
                  return redirect(request.GET.get('next') or 'reviews:index')
          
          # request method가 GET 혹은 유효성 검사 실패한 사용자의 입력값이라면
          else:
              # 빈 폼 혹은 오류 메시지를 출력하는 폼
              forms = AuthenticationForm()
              
          context = {
              "forms" : forms,
          }
          return render(request, "accounts/login.html", context)
      ```

      

3. 사용자의 입력값을 받아올 폼을 템플릿에 출력한다.(`accounts` > `templates` > `accounts`> `login.html`)

   ```python
   {% extends 'base.html' %}
   {% load django_bootstrap5 %}
   {% block content %}
   
     <div class="w-25">
       <form action="" method="POST" class="fw-bold">
         <div class="h4 pb-2 mb-4 text-black fw-bold border-bottom border-secondary">
           로그인
         </div>
         {% csrf_token %}
         {% bootstrap_form forms %}
         <div class="text-end d-grid">
           <input type="submit" class="btn btn-outline-black" value="로그인">
         </div>
       </form>
     </div>
   </div>
   {% endblock %}
   ```

   

## 회원 목록 조회(index)

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`accounts` > `urls.py`)

   ```python
   path("", views.index, name="index")
   ```

2. url을 추가했으면 `views`로 가서 `index`함수를 정의한다.(`accounts` > `views.py` )

   `index`함수는 가입된 회원 목록을 조회하는 템플릿을 출력하는 함수이다.

   

   회원 목록은 모든 회원의 유저객체를 담고 있다.

   ```python
   def index(request):
       # 회원 정보를 가지고 있는 유저 객체
       infos = get_user_model().objects.all()
       context = {
           "infos" : infos,
       }
       
       # 유저객체에 대한 정보를 템플릿에 출력한다.
       return render(request, "accounts/index.html", context)
   ```

3. 회원 정보를 보여줄 템플릿에 출력한다.(`accounts` > `templates` > `accounts`> `index.html`)

   회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동할 수 있도록 `username`에 링크를 걸어준다.

   모든 회원의 회원 아이디를 각각 출력해야하므로 `for`문 순회를 통해 접근한다.

   회원 정보는 `context`에서 `infos`로 받아왔다.

   ```html
   {% extends 'base.html' %}
   {% load django_bootstrap5 %}
   {% block content %}
     <div>
       {% for info in infos %}
         <div>
           <hr>
           <a href="{% url 'accounts:detail' info.pk %}" class="text-decoration-none">
             {{ info.username }}
           </a>
         </div>
       {% endfor %}
       <hr>
     {% endblock %}
   ```

   

## 회원 정보 페이지(프로필 페이지)

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`accounts` > `urls.py`)

   ```python
   path("/<int:user_pk/", views.detail, name="detail"),
   ```

   - 오류 발생(해결 : `/` 제거)

     ```python
     path("<int:user_pk>", 💡 문제 해결 views.detail, name="detail"),
     ```

     

2. url을 추가했으면 `views`로 가서 `detail`함수를 정의한다.(`accounts` > `views.py` )

   `detail` 함수는 <u>특정 회원</u>의 정보를 보여주는 템플릿을 출력하는 함수이다.

   회원의 정보는 유저 객체에 저장되어 있고, 모든 회원이 아닌 특정 회원 하나의 정보를 가져오므로 `get` 메소드를 사용하여 조회하고자 하는 회원의 유저 객체를 가져올 수 있다.

   ```python
   # 회원 정보 조회
   def deatil(request, pk):
       # 요청으로 들어온 pk가 일치하는 유저 객체를 저장(조회하고자 하는 회원의 페이지)
       info = get_user_model().objects.get(pk=pk)
       context = {
           "info" : info,
       }
       return render(request, "accounts/detail.html", context)
   ```

   - 오류발생(해결: path의 동적인자와 views함수의 매개변수 일치시키기)

     ```python
     path("<int:user_pk>", views.detail, name="detail"),
     ```

     ```python
     def detail(request, user_pk): 💡 문제 해결
         # 요청으로 들어온 pk가 일치하는 유저 객체를 저장(조회하고자 하는 회원의 페이지)
         info = get_user_model().objects.get(pk=user_pk)
         context = {
             "info" : info,
         }
         return render(request, "accounts/detail.html", context)
     ```

     

3. 조회하고자 하는 회원의 정보를 보여줄 템플릿에 출력한다.(`accounts` > `templates` > `accounts`> `detail.html`)

   회원의 정보는 `context`에서 `info`로 받아왔다.

   회원 정보 수정은 링크로 통한다.

   ```html
   {% extends 'base.html' %}
   {% load django_bootstrap5 %}
   {% block content %}
     <div class="card" style="width: 18rem;">
       <div class="card-body">
         <h5 class="card-title">{{ info.username }}</h5>
         <h6 class="card-subtitle mb-5 text-muted">가입일 |
           {{ info.date_joined | date:"Y-n-j" }}
         </h6>
         <p class="card-text">{{ info.email }}</p>
         <a href="{% url 'accounts:update' info.pk %}" class="card-link">회원 정보 수정</a>
       </div>
     </div>
   {% endblock %}
   ```



## 회원 정보 수정

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`accounts` > `urls.py`)

   게시글을 업데이트할 때는 해당 글의 `pk`를 가져와서 객체의 인스턴스를 갱신했다.

   하지만, **회원 정보 수정 페이지를 로그인한 유저만 접근 가능하도록 하면**, 로그인되어 있는 유저의 <u>pk 값은 받아올 필요가 없다.</u> 따라서, path의 주소 설계도 게시글 수정 url과 달리 동적인자가 없는 형태로 이뤄진다.

   ```python
   path("update/", views.update, name="update"),
   ```

2. url을 추가했으면 `views`로 가서 `update`함수를 정의한다.(`accounts` > `views.py` )

   `update` 함수는 `request.method`에 따라 `GET`일 때는 빈 수정 폼을 보여주는 템플릿을 출력하고, `POST`일 때는 사용자가 입력한 값을 DB에 저장하는 함수이다.

   📌 수정 성공 이후의 처리는 기획의 영역이다.

   

   회원정보 수정 폼은 회원가입 폼처럼 모델 폼의 상속을 받는, `django.contrib.auth.forms`의 `UserChangeForm`을 사용한다. 기본 `UserChangeForm`은 `model`이 `auth.User`로 설정되어있으므로, 상속하여 `model`속성을 재정의한 수정 폼이 필요하다.

   

3. 회원정보 수정 폼으로 사용할 모델폼을 생성한다.(`accounts` > `forms.py` )

   회원정보 수정 폼의 `model` 속성은 `accounts.User`가 되어야 한다. 그러면서 `UserChangeForm`의 속성과 메서드를 그대로 사용할 것이기 때문에 클래스 상속의 형태로 회원정보 수정 폼 생성이 이뤄진다.

   ```python
   from django.contrib.auth.forms import UserChangeForm
   ```

   

   회원정보 수정 폼에서 수정되는 내용은 (일반적으로 username은 제외한다.) `field`속성에서 정할 수 있다.

   📌 기획(명세)에 따라 작성한다.

   ```python
   fields = ("first_name", "last_name", "email",)
   ```

   완성된 회원정보 수정 폼은 다음과 같다. `UpdateForm`

   ```python
   from django.contrib.auth import get_user_model
   from django.contrib.auth.forms import UserChangeForm
           
   class UpdateForm(UserChangeForm):
       class Meta:
           model = get_user_model()
           fields = ("first_name", "last_name", "email",)
   ```

   

4. 모델 폼을 추가했으면 `views`로 가서 `update`함수를 수정한다.(`accounts` > `views.py` )

   `update` 함수에서 사용할 회원정보 수정 폼은 `UserChangeForm`을 상속받아 재정의한 `UpdateForm`을 가져온다.

   ```python
   from .forms import UpdateForm
   ```

   `request.method`가 `GET`일 때는, 회원정보 수정 폼을 보여주되, 게시글 수정 때처럼 이전에 저장돼 있던 입력값이 남아있어야 한다.

   ```python
   forms = UpdateForm(instance="request.user")
   ```

   `POST`일 때는 유저가 입력한 값을 저장하고, 프로필 페이지로 돌아간다.

   ```python
   # 회원 정보 수정
   def update(request):
       if request.method == "POST":
           forms = UpdateForm(request.POST, instance="request.user")
           if forms.is_valid():
               forms.save()
               # 수정이 완료되면 수정한 회원의 정보 보기 페이지로 보낸다.
               return redirect("accounts:detail", request.user.pk)
       else:
           forms = UpdateForm(instance="request.user")
       
       context = {
           "forms" : forms,
       }
       return render(request, "accounts/update.html", context)
   ```

   `accounts/update/`는 로그인한 사용자만 접근할 수 있도록 `urls.py`에서 설정하였으므로, `django.contrib.auth.decorator`에서 제공하는 `@login_required`를 사용한다. 

   ```python
   from django.contrib.auth.decorators import login_required
   ```

   ```python
   # 회원 정보 수정
   @login_required
   def update(request):
       if request.method == "POST":
           forms = UpdateForm(request.POST, instance="request.user")
           if forms.is_valid():
               forms.save()
               # 수정이 완료되면 수정한 회원의 정보 보기 페이지로 보낸다.
               return redirect("accounts:detail", request.user.pk)
       else:
           forms = UpdateForm(instance="request.user")
       
       context = {
           "forms" : forms,
       }
       return render(request, "accounts/update.html", context)
   ```

   - 오류 발생(해결 : `" "` 제거)

     ```python
     # 회원 정보 수정
     @login_required
     def update(request):
         if request.method == "POST":
             forms = UpdateForm(request.POST, instance=request.user) 💡 문제 해결
             if forms.is_valid():
                 forms.save()
                 # 수정이 완료되면 수정한 회원의 정보 보기 페이지로 보낸다.
                 return redirect("accounts:detail", request.user.pk)
         else:
             forms = UpdateForm(instance=request.user) 💡 문제해결
         
         context = {
             "forms" : forms,
         }
         return render(request, "accounts/update.html", context)
     ```

5. 로그인한 회원에게 보여 줄 회원정보 수정 폼을 템플릿에 출력한다.(`accounts` > `templates` > `accounts`> `update.html`)

   ```html
   {% extends 'base.html' %}
   {% load django_bootstrap5 %}
   {% block content %}
     <form action="" method="POST" class="fw-bold">
       <div class="h4 pb-2 mb-4 text-black fw-bold border-bottom border-secondary">
         회원 정보 수정
       </div>
       {% csrf_token %}
       {% bootstrap_form forms %}
       <div class="text-end d-grid">
         <input type="submit" class="btn btn-outline-black" value="수정">
       </div>
     </form>
   
   {% endblock %}
   ```

   

   로그인한 회원만 회원 수정 페이지를 볼 수 있도록 회원 프로필 페이지에서 `if`문을 활용하여 수정한다. (`accounts` > `templates` > `accounts`> `detail.html`)

   템플릿 변수 `{{ user }}`를 활용해서 반환되는 유저 객체의 pk값(현재 로그인한 회원의 pk값)과 프로필 페이지에서 보여주고 있는 유저 객체의 pk값이 같으면 수정 페이지 링크를 볼 수 있도록 한다.

   📌 템플릿 변수 `{{ user }}` 는 `context`로 보내지 않아도 사용할 수 있다.

   ```html
   {% if user.pk == info.pk %}
   <a href="{% url 'accounts:update' %}" class="card-link">회원 정보 수정</a>
   {% endif %}
   ```



## 로그아웃

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`accounts` > `urls.py`)

   ```python
   path("logout/", views.logout, name="logout"),
   ```

2. url을 추가했으면 `views`로 가서 `logout`함수를 정의한다.(`accounts` > `views.py` )

   `logout`함수는 요청이 들어오면 <u>DB의 세션에서 사용자를 꺼낸다.</u> 로그아웃 후의 처리는 기획의 영역이다.

   ```python
   from django.contrib.auth import logout as auth_logout
   ```

   ```python
   def logout(request):
       auth_logout(request)
       return render(request, "base.html")
   ```



## 네비게이션 바

1. 네비게이션 바는 모든 페이지에서 보여야 하므로, `base.html`에서 작성한다.

2. `static` 파일을 활용하여 `css`스타일을 적용한다.

   `base.html`에서 사용될 것이므로 `staticfiles`의 기본 경로 이외의 경로를 추가한다.(`프로젝트 폴더` >`settings.py` )

   📌 `staticfiles`의 기본 경로는 `app/static/`이다.(day8 django)

   ```python
   STATIC_URL = '/static/' # 기본 경로
   
   STATICFILES_DIRS = [BASE_DIR/'static'] # 추가 경로
   ```

   `static`파일을 활용하기 위해서는 템플릿의 상단에 `{% load static %}` 을 추가하고, html의 `<link>`로 불러와야 한다.

   ```html
   {% load static %}
   <link rel="stylesheet" href="{% static '/style.css' %}">
   ```

   기획(명세)에 따라 구성한다.

   ````
   - 리뷰 목록 페이지 이동 버튼
   - 리뷰 작성 페이지 이동 버튼
   - 비 로그인 유저는 작성 버튼 출력 X
   - 로그인한 사용자의 username 출력
   - username을 클릭하면 회원 조회 페이지로 이동
   - 로그아웃 버튼
   - 비로그인 상태라면 로그인, 회원가입 페이지 이동 버튼 출력
   ````



## 리뷰 생성

1. 리뷰 생성 기능은 새로운 앱(`reviews`)에서 기능할 것이므로 새로 앱 등록을 한다.

   ```bash
   (venv) 
   $ python manage.py startapp reviews
   ```

   앱을 생성하였으면 앱 등록을 한다.(`프로젝트 폴더` > `settings.py`)

   ```python
   INSTALLED_APPS = [
       'accounts',
       'reviews',
   ```

2. 앱 등록을 했으니 url을 추가한다.(`프로젝트 폴더` > `urls.py`)

   ```python
   path('reviews/', include("reviews.urls")),
   ```

   `앱 폴더`에 `urls.py`를 추가하고, url을 추가한다.(`reviews` > `urls.py`)

   ```python
   from django.urls import path
   from . import views
   
   app_name = "reviews"
   
   urlpatterns = [
       path("create/", views.create, name="create")
   ]
   ```

3. url을 추가했으면 `views`로 가서 `create`함수를 정의한다.(`reviews` > `views.py` )

   `create` 함수는 `request.method`가 `GET`일 때 사용자의 입력 값을 받아올 폼을 보여주는 템플릿을 출력하고, `POST`일 때 받은 입력 값을 DB에 저장한다.

   📌 함수는 정상 작동하는지, 잘못 매칭된 url 은 없는지, 템플릿을 잘 가져오고, 상속받고 있는지 확인하기 위해 처음부터 함수를 정의하기보다는 서버를 먼저 돌려본다.

   ```python
   def create(request):
       return render(request, "reviews/create.html")
   ```

4. `views`함수를 실행시킬 템플릿 파일을 생성한다.(`reviews` > `templates` > `reviews` > `create.html`)

     ```html
     {% extends 'base.html' %}
     {% block content %}
      <h1>함수 정상 작동 확인합니다.</h1>
     {% endblock %}
     {% block aside %}{% endblock %}
     ```

5. 서버가 잘 돌아가는지 확인했으면, `views` 함수를 수정한다. (`reviews` > `views.py`)

   `create` 함수는 `GET`일 때 빈 게시글 작성 폼을 보내주는 템플릿을 출력하고, `POST`일 때 사용자가 입력한 값을 DB에 저장하는 함수이다. 

   

   게시글 작성 폼은 `Review`를 모델로 하는 모델폼을 사용한다.

   모델폼은 `django.forms`의 `ModelForm`을 상속받는다.

   

   `model`을 반영하기 위해서는 모델이 필요하므로 모델 먼저 정의한다.

6. `Review`모델을 기획(명세)에 따라 정의한다.(`reviews` > `models.py`)

   ````python
   from django.db import models
   
   # Create your models here.
   class Review(models.Model):
       title = models.CharField
       content = models.TextField
       movie_name = models.CharField
       grade = models.IntegerField
       created_at = models.DateTimeField(auto_now_add = True)
       updated_at = models.DateTimeField(auto_now = True)
   ````

   모델이 정의 되었으면, 마이그레이션을 진행한다.

   ```bash
   $ python manage.py makemigrations
   ```

   - 오류 발생(해결 : `null=True` 추가)
   
     ```python
     from django.db import models
     from django.core.validators import MinValueValidator, MaxValueValidator
     
     # Create your models here.
     class Review(models.Model):
         title = models.CharField(max_length=80, null=True) 💡 문제 해결
         content = models.TextField(null=True) 💡 문제 해결
         movie_name = models.CharField(max_length=40, null=True) 💡 문제 해결
         grade = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], null=True) 💡 문제 해결
         created_at = models.DateTimeField(auto_now_add = True)
         updated_at = models.DateTimeField(auto_now = True)
     ```

7. 게시글 작성 폼으로 보여줄 모델 폼을 생성한다.(`reviews` > `forms.py`)

   모델폼은 `django.forms`의 `ModelForm`을 상속받는다.

   ```python
   from django.forms import ModelForm
   ```

   기획(명세)에 따라 폼에서 보여줄 필드값을 정의한다.

   📌 `class Meta` 철자에 주의한다.(`meta`는 인식하지 못하기 때문)

   ```python
   from django import forms
   from .models import Review
   
   class PostForm(forms.ModelForm):
       
       class Meta:
           model = Review
           fields = ("title","content", "movie_name", "grade",)
   ```

8. 게시글 작성 폼을 만들었으므로 `views`함수를 수정한다.

   `GET`일 때는 작성 폼이 있는 템플릿을 출력한다.

   `POST`일 때는 사용자가 입력한 값이 유효성 검사를 통과하면 DB에 저장한다.

   유효성을 통과하지 못하면, 오류 메시지를 출력하는 폼을 `context`로 보낸다.

   게시글 작성은 로그인한 사용자만 작성할 수 있으므로 `@login_required`를 활용한다.

   ```python
   from django.shortcuts import render
   from .forms import PostForm
   from django.contrib.auth.decorators import login_required
   
   @login_required
   def create(request):
       if request.method == "POST":
           
           forms = PostForm(request.POST)
           # 사용자가 입력한 값이 유효성을 통과하면 DB에 저장한다.
           if forms.is_valid():
               forms.save()
               return render(request, 'base.html') 
       # request.method 가 GET일 경우
       else:
           # 빈 폼
           forms = PostForm()
       context = {
           "forms" : forms,
       }
       return render(request, "reviews/create.html", context)
   ```

9. `views`함수를 정의했으면 게시글 작성 폼을 보여줄 템플릿을 구성한다.(`reviews` > `templates` > `reviews` > `create.html` )

   ```html
   {% extends 'base.html' %}
   {% load django_bootstrap5 %}
   {% block content %}
     <form action="" method="POST">
       {% csrf_token %}
       {% bootstrap_form forms %}
       <input type="submit" class="btn btn-primary">
     </form>
   {% endblock %}
   {% block aside %}{% endblock %}
   ```



## 리뷰 목록 조회

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`reviews` > `urls.py`)

   ```python
   path("", views.index, name="index"),
   ```

2. url을 추가했으면 `views`로 가서 `index`함수를 정의한다.(`reviews` > `views.py` )

   `index` 함수는 `request.method`가 `GET`일 때 리뷰 목록을 보여주는 템플릿을 출력하는 함수이다.

   DB에 저장된 모든 `Review` 객체를 보여주는 것이므로 `Review` 모델이 필요하다.

   ```python
   from .models import Review
   ```

   ```python
   def index(request):
       reviews = Review.objects.order_by("-pk")
       context = {
           "reviews" : reviews,
       }
       return render(request, "reviews/index.html", context)
   ```

3. 리뷰 목록을 보여줄 템플릿에 출력한다.(`reviews` > `templates` > `reviews`> `index.html`)

   모든 리뷰 객체를 `context`에서 `reviews`라는 변수로 받아왔다.

   각 리뷰 객체의 제목 `title`필드의 값을 출력하려면 `for`문으로 순회한다.

   리뷰 목록에서 리뷰별 제목을 클릭하면 해당 리뷰의 상세 페이지로 이동한다.



## 리뷰 정보 조회

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`reviews` > `urls.py`)

   리뷰 정보 페이지는 특정 리뷰에 대한 정보를 출력하므로 조회하고자 하는 `Review` 객체의 `pk`값이 필요하다.

   📌 동적인자의 매개변수는 `views` 함수의 매개변수와 일치해야한다.

   ```python
   path("deatil/<int:review_pk>", views.detail, name="detail"),
   ```

2. url을 추가했으면 `views`로 가서 `detail`함수를 정의한다.(`reviews` > `views.py` )

   `detail` 함수는 특정 리뷰의 정보를 출력하는 함수이다.

   특정 리뷰의 정보는 `Review` 객체가 가지고 있고, 조회하고자 하는 리뷰의 `pk`값과 일치하는 `Review` 객체를 가져오면 된다.

   ```python
   def detail(request, review_pk):
       review = Review.objects.get(pk=review_pk)
       context = {
           "review" : review,
       }
       return render(request, "reviews/detail.html", context)
   ```

3. 조회하고자 하는 리뷰의 상세 정보를 출력하는 템플릿을 구성한다.(`reviews` > `templates` > `reviews` > `detail.html`)

   리뷰의 정보를 출력하고, 상세 페이지에서 수정과 삭제로 접근할 수 있는 버튼을 보여준다.



## 리뷰 정보 수정

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`reviews` > `urls.py`)

   ```python
   path("<int:review_pk>/update/", views.update, name="update"),
   ```

2. url을 추가했으면 `views`로 가서 `update`함수를 정의한다.(`reviews` > `views.py` )

   `update` 함수는 `request.method` 가 `GET`일 때는 이전에 사용자가 입력한 내용이 있는 폼을 보여주는 템플릿을 출력하고, `POST`일 때는 사용자가 수정한 내용으로 DB에 저장하는 함수이다.

   사용자가 입력한 내용은 `Review` 객체가 가지고 있다.

   수정은 로그인한 사용자만 할 수 있도록 `django.contrib.auth.decorator`의 `login_required`를 활용한다.

   ```python
   @login_required
   def update(request, review_pk):
       review = Review.objects.get(pk=review_pk)
       # 요청이 POST로 들어온다면
       if request.method == "POST":
           forms = PostForm(request.POST, instance=review)
           if forms.is_valid():
               forms.save()
               # 수정 후 디테일 페이지로 돌아간다.
               return redirect('reviews:detail', review_pk)
       # 요청이 GET이라면
       else:
           # 사용자가 이전에 입력한 값만 있는 폼을 보여준다.
           forms = PostForm(instance=review)
       context = {
           "forms" : forms,
       }
       return render(request, "reviews/update.html", context)
   ```

3. 수정하고자 하는 리뷰의 수정 폼을 출력하는 템플릿을 구성한다.(`reviews` > `templates` > `reviews` > `update.html`)




## 리뷰 삭제

1. 새로운 기능을 구현할 것이므로 url을 추가한다.(`reviews` > `urls.py`)

   ```python
   path("<int:review_pk>/delete/", views.delete, name="delete"),
   ```

2. url을 추가했으면 `views`로 가서 `delete`함수를 정의한다.(`reviews` > `views.py` )

   `delete` 함수는 특정 게시글의 데이터를 삭제하는 함수이다.

   삭제 후 게시판 목록으로 보내도록 기획하였다.

   ```python
   def delete(request, review_pk):
       review = Review.objects.get(pk=review_pk)
       review.delete()
       return redirect('reviews:index')
   ```

   

# 문제상황 발생(10.14)

- 회원 정보 페이지 구현 단계에서 path에서 정한 동적 인자와 views함수의 매개변수가 일치하지 않아 오류가 발생하였다.

![image-20221014134918226](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221014134918226.png)



- 회원 정보 페이지 구현 단계에서 path의 주소를 설계할 때, `/`를 앞에 추가했더니 다음과 같은 오류가 발생하였다.

  ```bash
  Remove this slash as it is unnecessary. If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.
  ```

  

  ![image-20221014135028972](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221014135028972.png)

- 해결 

  path를 문법에 맞게 고쳐주고, (`"<int:user_pk>"`), 매개변수를 일치시켜줬더니 (`user_pk`) 정상적으로 동작하였다.



- 회원 정보 수정 구현 단계에서 모델 폼의 `instance`값을 문자열로 주면서 오류가 발생하였다.

  ![image-20221014153302777](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221014153302777.png)



- 해결

  `" "`를 제거하였다.



- 모델 생성 문법을 잘못 해서 `id`, `created_at`, `updated_at` 필드만 DB에 반영되었다.

  ![image-20221015100934889](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015100934889.png)

  ![image-20221015100825155](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015100825155.png) 

생성된 테이블에 필드를 추가하려고 하니 다음과 같은 오류가 발생하였다.

![image-20221015101129600](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015101129600.png)

![image-20221015101148488](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015101148488.png)

`content` 필드에 해당하는 `models.TextField()`의 default 값이 정해지지 않아서 발생한 오류이다. 이미 생성된 `reviews_review`테이블에 새로운 필드가 추가되면 이전에 존재하던 행들의 필드 값에 대해 <u>어떤 처리</u>가 필요하다는 의미의 메시지이다. 해결 방법은 두 가지이다. [원래 저장되어있던 객체들의 새로운 필드에 어떤 조치를 취해야한다는 메시지](https://jamanbbo.tistory.com/19)

1) default 값을 추가하거나, `null=True`를 추가한다.

   추가된 모든 필드에 `null=True`를 추가한다.

   ![image-20221015102138091](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015102138091.png)

   ![image-20221015102212253](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015102212253.png)

   DB에 정상 반영되는 것을 확인할 수 있다.

2) DB를 초기화한다.(`migtraion` > `__init__.py` 파일 제외 모두 삭제)

   존재하는 `reviews_review` 테이블을 삭제한다.[마이그레이션 초기화 및 db테이블 삭제](https://maximum-curry30.tistory.com/124)

   ![image-20221015104706911](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015104706911.png)

   삭제 후 새로 `makemigrations` 하면 `0001_initial.py` <u>마이그레이션 폴더가 생성되지만</u> 이를 DB에 반영하기 위해 `migrate`하면 다음과 같은 오류가 발생한다.

   ````
   No migrations to apply
   ````

   ![image-20221015104006724](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015104006724.png)

`initial.py` 파일을 새로운 테이블로 인식하도록 파일명(`0004_initial.py`)을 바꿔준다. (***정석이 아니기 때문에 지양하도록한다.**) [No migrations to apply 해결](https://velog.io/@haileeyu21/Error-dJango-migrate-%ED%96%88%EB%8A%94%EB%8D%B0-No-migrations-to-apply-%EC%9D%BC-%EA%B2%BD%EC%9A%B0)

![image-20221015104312904](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015104312904.png)

![image-20221015104913989](기능 구현 절차(로그인부터 게시판 CRUD까지).assets/image-20221015104913989.png)

DB에 정상 반영되는 것을 확인할 수 있다.



- 해결

  이미 존재하는 테이블의 추가 필드들에 `null=True`를 추가하였다.