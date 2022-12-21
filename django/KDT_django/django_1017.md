````
이미지 업로드를 구현하고 싶은데 어떤 설명글을 봐야 할까?
````

- 코드로 체크한다

````
Managing files
````

- 유저로부터 업로드받은 파일들에 접근하는 방식

- 이미지 필드 활용 방법을 알면 파일 필드를 활용하는 법을 아는 것과 같다고 볼 수 있다.

- ````
  Requires the Pillow library
  ````

- `Pillow library`?

**Python Imaging Library**

> 이미지를 관리하기 위해서(Python Image Library) > 왜 파이썬? > 장고가 파이썬기반이니까

1. pip install[대문자 'P'설치](https://pillow.readthedocs.io/en/stable/installation.html)

```bash
pip intall Pillow
```

git commit -m 'Image upload' - install pillow

2. Image Field 정의

   ImageField

   attributes

   - `upload_to` => 사용자가 업로드한 파일을 어디에 업로드할 건지, 

     항상 이미지를 업로드하진 않으니까 `blank = True`

3. `migrationgn`후  `migrate` 진행

   git commit -m 'Image-upload models'

4. DB에 image를 받을 수 있는 필드가 추가되었을까? -> O

   모델폼에는 Image를 받을 수 있는 필드가 추가 안되어있다 

5. `forms.py`에서 모델폼을 수정

6. 하지만! DB에 저장되지 않아!!

   html input + image 필드는 있음.

   유효성검사랑 저장은 잘 통과한 것을 확인했음. request값도 제대로 받아오는 거 같음.

7. HTEMLFormElement.enctype
8. File은 따로 request.Files 객체에 저장된다.

9. HTML에서 폼 옵션을 조정하고, views에서도 그 데이터를 어떻게 받아올 건지!

10. mideia root와 media fiels(`setting.py`)

    ```python
    MEDIA_ROOT = BASE_DIR / 'images'
    ```

    ```python
    MEDIA_URL = '/media/'
    ```

11. url에도 `MEDIA ROOT URL`을 추가



이미지를 받기 위해서는 각각의 설정이 필요했다.

`HTML Form(enctype)`

`views request.Files`



- 이미지 파일들의 용량이 너무 크다면, 로드하는 데 시간이 너무 오래 걸리는 문제점이 발생

- `django-imagekit` 라이브러리 사용

  ```bash
  pip install image-kit
  ```

- `settings.py`> `INSTALED_APPS` 에 `imagekit`추가

- 장고 이미지필드보다 더 많은 것을 해주는 `ImageSpecFields`

  원본 이미지를 keep할 필요가 없으면 프로세스 한다음에 저장하기만 하면, 프로세스 이미지필드 클래스를 사용

  <u>원본 자체를 썸네일로 저장해버린다.</u>

- 코드 긁어오기



## ValueErrror at /articles/2/

이미지가 없는 게시물인데 이미지를 받은 템플릿을 보여주려고 해서



## The message Framework





# 오후 실습(이미지 업로드)

## 데이터 생성

1. 앱을 생성한다.

   ```ㅠㅁ노
   $ python manage.py startapp uploads
   ```

2. 생성했으므로 등록한다.

   ```python
   INSTALLED_APPS = [
       'uploads',
   ```

   ```python
   LANGUAGE_CODE = 'ko-kr'
   
   TIME_ZONE = 'Asia/Seoul'
   ```

3. runserver

4. url 설정하고, views함수, 'base.html' 설정하고, runserver돌려보기

   ```python
       path('articles/', include("uploads.url")),
   ```

   ```python
   def create(request):
       return render(request, "uploads/create.html")
   ```

   ```python
   {% extends 'base.html' %}
   {% block content %}
     <h1>함수 정상작동 확인합니다.</h1>
   {% endblock content %}
   ```

5. 모델 정의하기

   모델 정의하는데 이미지 데이터 저장 필드 정의하기ㄴ

   1. `MEDIA_ROOT`, `MEDIA_URL` 설정

      업로드 된 파일의 경로는 django가 제공하는 'url'속성을 통해 얻을 수 있다

      

   2. URL을 설정했으면 MODEL field를 정의하고 마이그레이션 실행
   
   3. 모델을 정의했으므로 이미지를 받아올 모델폼을 정의
   
   4. 이미지를 받아올 폼을 출력할 views함수 정의
   
      파일은 `request.FILES` 객체로 받아오므로 `request.POST`이외의 매개변수를 추가해야 한다
   
   5. 템플릿에서 폼의 속성에 `method="POST"`이외에 `enctype="multipart/form-data"` 속성을 추가한다