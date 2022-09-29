# view details 

1. path 설정

   #요청 - 응답

   어떤 주소(detail/)로 요청하면

   어떤 view함수를 응답할까?

   path('deatil/', views.deatil, name='detail')



3. deatil 함수설정

   def detail(request):

   return render(request, 'posts'/new.html')

   글의 내용을 보여줘야 하므로 

   더미 데이터로 template에 하나 만들어보자



4. deatil.html

   base.html을 상속받기 위해 {% extends 'base.html' %}을 최상단에,

   {% block content %}

   ```dummy
   h1 detail.html
   
   h2 제목 : 오늘의 점심은?
   
   p 골라주세요.
   ```

   {% endblock %}



5. deatil 함수 정의

   get()메소드를 사용해서 특정 pk의 데이터를 불러온다

   불러온 데이터를 변수에 할당

   - pk를 어떻게 받아올 것인가?

     index.html에서 {% url 'posts:deatil' post.pk %}

     <u>url 뒤에 닫는 태그 사이에</u>

     동적인자로 전달하기

   - path에서도 `detail/<int:pk>` 추가

path에서 명시한 동적인자와 views 함수에서 받아오는 인자는 동일해야 한다.

6. deatil 함수 다시 정의

   Post.objects.get(pk = pk_)

7. detail.html 수정

   h2 {{ post.title }}



첫번재 read는 데이터의 목록을 출력하고,

두번째 read는 하나의 데이터에 대한 정보를 출력



내가 클릭할 component에 a태그로 링크를 걸어줍니다.

삭제를 할 때처럼 내가 클릭한 글의 pk 값을 동적인자로 전달 받아야 한다.(내가 보고싶은 글의 내용을 보고싶기 때문에)

그 다음엔 url을 만들고 view만들고 templates만들기

pk값을 이동시키면서(동적인자) 원하는 데이터를 view에서 가져오고 가져온 데이터를 templates에 출력하기



# update

사용자가 글을 수정하려면, 수정 페이지가 따로 존재해야 한다

수정을 하고 수정 버튼을 누르면 변경사항을 반영할 view가 필요하다

- 사용자의 입력을 받을



1. path 설정

   path("edit", views.edit, name="edit")



2. edit 함수설정

   def edit(request):

   return render(request, 'posts/edit.html')



3. edit에 대한 templates 작성

   new.html과 똑같이 가져와서

   h1 수정페이지

   form 

   기존의 데이터를 불러오기 위해 pk값을 동적 인자로 받는다.

   index.html 에서 {% url 'posts:edit' pk_%}

   

4. def edit(request, pk_):

   post = Post.object.get(pk=pk_)

   context = {"post" = post}



5. edit.html에서 

   input의 value에 views에서 넘겨온 {{ post.title }}과 {{ post.content }}를 각각 뿌려주기

   * textarea = > 큰 input (보통 글 작성할 때는 textarea 사용) textarea 태그는 value속성이 없으므로 태그 내부 값으로 작성해야 한다.



6. edit.html에서

   특정 pk를 가진 데이터를 불러오기 위해 pk를 동적 인자로 전달

   {% url 'posts:update' post.pk %}

   

7. url에서 path 추가

   path(`'update/<int:pk_>`, view.update, name='update'),

   

8. def update(request, pk_) url의 동적인자와 views에서 받는 인자가 동일

   update할 특정 데이터를 불러온다 = > pk_를 사용해서

   post_ = Post.objects.get(pk=pk_)

   title_ = request.GET.get('title')

   content = request.GET.get('content')

   

   데이터를 수정

   post.title = title_

   post.content = content_

   생성이 아니기 때문에 save()를 해줘야 한다.

   post.save()

   데이터의 디테일 페이지로 리다이렉트

   return redirect('post:details', post.pk) 내가 불러온 post의 pk를 인자로 추가

특정 글의 detail을 불러오려면 pk가 필요하므로 => 방금 수정한 글의 detail을 확인하기 위해서



업데이트는 read + create + 알파

read = 수정페이지에 데이터를 출력

