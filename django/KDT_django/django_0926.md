# variable routing

> url 주소를 변수로 사용하는 것을 의미



- form - input

  form에서 받은 html

  h1 fake 궁합앱

  당신의 이름 : input type

  그 분의 이름 : input type = submit

- 데이터를 어떻게 넘겨 받을 것인가 ?

  - 파라미터로 받기(form)
  - get, post

- 데이터를 보내고 가져오기

  - sending form data(client)

    h1

    form action="https://www.naver.com"

    Naver: input

    input type=submit

    /form

- 프로젝트는 어플리케이션의 집합

  - Retrieving the data(ping에서 보낸 데이터를 pong으로 가져와서 핸들링하기)
  - request 객체 살펴보기

- 템플릿 상속

  코드의 재사용성에 초점을 맞춘다

  - 모든 템플릿에 부트스트랩을 적용하고 싶으면 어떻게 할까 ?
    - 버전이 달라진다면 ?
  - DTL 에서 지원하는 템플릿상속
    - 부모 템플릿을 하나만든다
    - 상위 템플릿의 요소를 만들어서 저장해둔다.
    - extends 부모에서 쓰이는 것을 확장해서 자식에게 쓰겠다
    - 선택자만 바꾸면 (content 대신) 여러 blcok을 활용할 수 있다.





# 오전 실습 복습

> 루트페이지 만들기

- 패스 지정
  - from appp import views
  - path("", views.index),
- index 함수
- templates
- runserver



- variable parameter(동적 인자를 활용)

  - path("number/<int:number>", views.print_number),

  - def print_number(request, number):

    context = {

    #템플릿 변수 이름 : 값

    "number": number,}

    return render(request, "number.html", context)

  - number.html

    {{ number }}



- 3번 4번

  - form

    action=print-text.html <= 왜 이렇게 적은 것임

    input name="_text"

    input type="submit"

   - path("print-text/", views.print_text)

   - def print_text(request)

     text = request.GET.get('_text')

     context {

     #'템플릿 파일 변수이름' : 값

     "template_text" : text,}

     return render(request, "text.html", context)

  - text.html

    h1 text.html

    {{ "template_text" }}

- 받은 데이터를 받아오기

  

form 을 이용해서 값을 받아오는 것과 url을 이용해서 값을 받아오는 것의 차이

form 은 사용자의 입력이 필수, 하지만 입력을 받지 않는 게시글이나 뉴스글들은 어떻게 가져오지? => url을 이용해서 값을 받아온다.(주소값에 직접 값을 받는 형태)