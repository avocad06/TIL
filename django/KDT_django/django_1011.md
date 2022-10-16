# Django Auth

- '회원가입' 게시판이란 무엇이 같고, 무엇이 다를까?

  객체를 저장하고 관리한다는 점은 같다.

  그렇다면 다른 점은 무엇일까?

- Django Auth 개요

  > 인증과 권한을 함께 제공(처리)

- User모델 상속관계가 단계적으로 구조화되어 있는 이유

  > 필요한 부분만 갖다 쓰라고 ?

- 단방향 해시함수 : 암호화는 할 수있되 복호화는 불가능함(역산이 되면 안됨)
  - MD5 : 복호화하는 알고리즘이 이미 존재
  - SHA1 
  - SHA256 : django가 채택하고 있는 방식

- 회원가입

- 왜일까? 왜 직접 참조하지 말라고 하는 걸까?
- manager = ORM 관련 객체



# 원페이지 정리

우리가 활용하고 있는 건 User, 이미 장고에 구현이 되어 있다.

djngo 내부 구현(그 예로 admin)

어느 정도까지 구현이 되어 있냐하면 인증과 권한까지 구현이 되어 있다.

기본설정이 인증과 권한까지 구현되어있는 프레임워크는 찾기 힘들다. 그정도로 장고가 편하다 

form과 views.py에서 쓸 수 있는 메소드를 제공

article이라는 모델을 내부 기능으로 쓰는가 ? x

createsuperuser, admin 등의 기능을 django도 쓴다

유저모델을  account.User로 쓸 거야, 라고 settings.py에 Auth_User_Model 변수에 저장



회원가입 기능을 구현하면서 사용한 UserCreationForm

User라는 클래스를 사용하는데, 이는 Abstract User로부터 상속을 받는다.

그리고 Abstract User(username, email)는 AbstractBaseUser(비밀번호 암호화)를 상속받는다.

암호화와 인증을 구현하기 너무 복잡하고 힘들기 때문에, 이를 베이스로

form 도 User CreationForm을 제공(forms.ModelForm 상속)

<u>어떠한 모델의 어떤 필드를 폼에서 사용하고 관리 하겠다.</u>

Model Field를 관리(HTML Form 형성, 유효성 검사)

바로 쓰지는 못했는데 그 이유는?

class Meta : 

model = User 라고 되어있는데 이 User는 Auth의 User를 의미하고 있기 때문에,

account에 정의한 User로 의미하게끔 상속받아서 커스텀

User는 변경이 될 수가 있다. 때문에 모델에서 직접 꺼내쓰지말고 get_user_model()에서 참조해서 쓰자. 언제든 변경될 수 있으니, 직접 참조 하지 말자.



django.contrib이 의미하는 것은 무엇일까?

장고가 도와주는 기능

일반적인 웹 개발 문제들을 해결해주는 옵셔널하고 extra 적인 툴

범용적으로 쓸 수 있도록 패키지화 해준 것



# 오후 실습 및 복습

1. accounts 라는 **유저관리 앱 기능**을 새로 만들었으므로, 이에 대한 url이 필요하다.

2. url 만들었으면 모델 정의하러 감.(User 모델)

   1. 모델을 auth앱에서 가져와서 사용할 것 => **클래스 상속**을 통해서(`Django AbstractUser` 모델 상속)

      ```python
      from django.db import models
      from django.contrib.auth.models import AbstractUser
      ```

      

   2. 어떻게? <u>Custom User Model 로 대체하기</u>

   3. `settings.py`에서 `'auth.user'`를 변경

   4. `models.py`에서 클래스 상속

      1. 어디로부터 상속? `AbstractUser`

3. views 대강 적어놓고

4. html로 이동 => html에 **회원가입 폼이 필요하다.**

   views에서 `import UserCreationForm`

5. 정상적으로 출력되는 거 확인했으면 메소드 분리해서 유효성 검사까지 진행하기

6. 오류가 난다. manage 모델의 메서드를 사용하지 못했다

   1. 원인 => auth.user에서 accounts.user로 바꿨기 때문에
   2. `UserCreationForm`은 `ModelForm`을 상속받고 있다. 모델폼은 `auth.models`의 `User`모델을 상속 받고 있었다. => 그럼 `accounts`의 모델로 바꿔줘야됨. => 클래스 상속으로!

7. 앱 안에 `forms.py`를 만들어서 모델폼을 상속

   1. `UserCreationForm`을 상속받아서,(속성과 메소드를 재사용)

      - 메소드 오버라이딩 : 원래 기능을 유지하면서 <u>새로운 기능을 덧붙일 때</u> 사용

   2. 그 폼안의 모델 정보를(`class Meta:`) accounts의 model `User`로 바꿔준다.

      ````python
      from django.contrib.auth.forms import UserCreationForm
      from .models import User
      ````

      ```python
      class CustomUserCreationForm(UserCreationForm):
          
          class Meta:
              model = User
              fields = '__all__' 
      ```

8. 상속받은 모델 폼을 views.py 에 적용하기

9. Substituting a custom User model(django docs)

​	Referencing th User model

​	User 모델을 <u>직접 참조하지 말고 함수로 참조하기</u>