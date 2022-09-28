메인 문지기와 서브 문지기 개념으로 url을  각각 핸들링할 수 있게 

include()

앱이 두 개가 되면서 기능상으로는 문제가 없지만, 점점 앱이 많아지면 url이 너무 많아짐

=> 각각의 앱에서 URL을 관리



앱별로 각기 다른 이름공간을 가지게 됨. Namespace

특정 주문서마다 이름공간이 있다.

앱을 두 개로 나눴다면, pages랑 articles는 각기다른 

{% url 'greeting' %}



articles

index/ 라고 하는 주소에 name='index' 라고 변수명을 짓는 것처럼 이름을 선언해놨음.

create.html에서 {% url 'index' %}로 바꾸고

urls.py에서 name='index'라고 정의해놓으면 



index.html의 action 바꿔보기

path('create/', vews.creat, name='create'),

index.html로 가서 form 의 action에 "/articles/create"를 {% url 'create'%} 라고 수정

=> 직접 쓴 게 아니라 장고 DTL이 url을 해석?해줘서 표기됨 

변수화를 하면 유지보수 관점에서 만약 url이 변경되는 등의 상황에서 코드의 재사용성을 높일 수 있음.

문제가 될 수 있는 부분들:

practices앱에서도 name='index'로 한다면?

문제가 되지 않을까? 모든 영역에 공통적용이 되기 때문에 아까 articles/create 였던 index가 practices/index 로 가게 됨.



index라고 하는 링크가 중복되어 있는 상황 =>  URL namespace 로 해결해보자

app_name attribute를 작성해 URL namespace를 설정하자

그냥 index가 아니라 어떤 앱의 index인지 확인하고 갈게요

url tag의 변화 => {% url 'index' %}에서 {% url articles: create %}



app_name을 지정한 이후에는 app_name:url_name 형태로만 사용해야 한다.

app_name과 url을 구분하는 ':' 연산자



Template namespace

각기 다른 템플릿 내에 폴더로 나눠서 사용하는 것(이름 공간을 두는 것)

=> 디렉토리 생성을 통해 물리적인 이름공간을 구분



namespace라고 하는 것은 변수명이 어디까지 영향을 미치는지, 어떻게 다른 기능과 분리할지

-> 관심사의 분리, 유지보수의 용이성



Naming URL patterns



**DRY** 원칙

Don't Repeat Yourself

좋은 코드가 필요함. 코드의 효율성보다는 유지보수가 가능한 사람이 이해하기 좋은 코드가 좋은 코드. <u>코드리뷰 역량</u>(클린코드와 디자인패턴, TDD)

동일한 코드가 반복되지 않게

ex) base.html, urls namespace, 



django의 설계 철학(templates System)

표현과 로직을 분리(templates과 views 를 분리)

1. 표현 = templates( 사람들이 봐야될 페이지 )

   템플릿 시스템을 표현을 제어하는 도구

2. 중복을 배제



Framework의 성격

- 독선적

  Convention Over Configuration 설정보다는 관례를 따를 것

  따르게끔 만드는 프레임워크

  장고가 이에 해당

- 관용적

  자바, 스프링 등의 framework가 해당



django framework의 성격

- 다소 독선적
- 프레임워크는 우리가 하는 개발을 방해하기 위해 규칙, 제약을 만들어놓은 것이 아니다
- 우리가 온전히 만들고자 하는 것에만 집중할 수 있게 도와주는 것



django 구조 이해하기(MTV Design Pattern)

```
SW 다루는 직군

-> 세상 문제 해결

-> 세상의 문제는 너무 복잡해

-> 추상화 (요약)

복잡한 문제들을 추상화하는 스킬 = 디자인패턴, 구조
```



- 디자인 패턴이란 ?

  = 설계(무언가를 만든다, 설계한다)

  ex) 광안대교와 같은 현수교는 이전 사람들이 검증해온 공법 등

  일반화한 공법

- 소프트웨어 디자인 패턴

  클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나이다.

  자주 사용되는 소프트웨어의 구조를 마치 건축의 공법처럼 일반적인 구조화를 해둔 것

- MVC 소프트웨어 디자인 패턴

  관심사에 따른 분리(<u>유지보수에 용이</u>)

  - **Model** : 데이터와 관련된 로직은 관리
  - **View** : 레이아웃과 화면을 처리
  - **Controller** : 명령을 model과 view 부분으로 연결

​	=> 각자가 잘하는 것을 하자

- 장고는 M**TV**

  		- model 은 db이고 db는 model이다

  		- template 화면상의 사용자(html)
  		- view model&template과 관련한 로직을 처리해서 응답을 반환



django model

> database를 관리하는 로직

- db는 엑셀이다

- 스키마
  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
- 모델
  - 장고는 모델을 통해 데이터에 접근하고 조작을 한다
  - class Article
  - 클래스 상속이 뭘까?
  - 어떤 데이터가 들어갈지 통제를 해야 데이타베이스의 경량화, 원하는 방식의 통제가 가능해짐.
- 마이그레이션
  - migration을 하면 
  - migrate는 실제 데이터베이스에 반영하는 과정
  - 모델을 정의하거나 수정하게 되면 migration 과정을 거쳐야 한다





# 앱 만들기

python manage.py startapp posts

메인문지기에

path("posts/", include("posts.urls")), 추가

posts 앱 안에 urls.py 생성

name=index, index를 전역으로 인식할 수 있으므로 app_name="posts"로 선언

 templates를 만들고 그 안에 또 posts폴더 만들기

그리고 그 안에 index.html

게시물을 클릭해서 내용물이 보이는 구조

a 링크 안에 url namespace posts.new



posts/create/title=안녕하세요+반갑습니다&content=냉무

# TemplateDoesNotExist at /posts/create/

tmplates/posts 폴더에 create.html 템플릿 작성

context에서 가져온 {{ title }}



DB에 저장하려면?

models.py 로 들어가서 구조를 설정해주기

필드를 정의한다 = 장고가 가져다 준 모델 orm으로 객체처럼 만들어줘

models 작업이 끝나면

makemigrations

manage.py migrate

db에 저장하는 로직

Post.objects.create()

from .models import Post



목록으로 링크를 만들고 돌아갔지만 아직 보여주는 로직이 없기 때문에

저장만 되어있고 DB로부터 가져와서 보여주는 로직을 짜야 함

veiws.py 에서 



for문 돌려서 객체 안에 있는 내용 호출해서 출력하기



쓰면 내용 바로 보고싶은데 꼭 작성완료 홈페이지로 가네

작성완료 홈페이지로 가게 되면 리다이렉션으로 게시판의 메인으로 보내주기



rdturn render가 아니라 장고redirect

redirect는 어떤 parameter들을 요구하나요 ?



우선은 import render에 redirect도 같이 추가해주기

posts/index/ 라고 해도 되고, posts:index로 해도 된다



새글을 쓰면 바로 메인으로 돌아간다



중요한 건 로직보다 사용성이다.



수정 및 삭제

li 닫기 전에 a태그 2개 추가하면 글마다 수정, 삭제



수정/삭제는 id값(PK)이 필요하다.

반복문 안에 post.id 값도 같이 출력해보면 각각 고유의 id값을 가지고 있는 것을 볼 수 있음.

동적 파라미터로 삭제페이지를 구성할 것



delete과정

get pk 



# 오후 오전복습

migrate = 이주하다

만들어놓은 청사진은 데이터베이스에 이주시킨다.



include는 공간을 분리하는 느낌

app_name을 지정하는 것은 소프트웨어적으로 나누는 것



max_length

