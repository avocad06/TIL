# view details 

````
1. path 설정
2. views.detail
3. detail.html
4. views.detail
5. detail.html
````

```
views와 template을 왔다리갔다리하며 수정
```

```
특정 글의 상세내용이므로 동적인자를 필요로 한다.
```



1. path 설정

   > url은 요청과 응답
   >
   > url 은 어떤 주소(/detail)로 요청하면 어떤 함수(views.detail)로 응답해야 할까?

   ```py
   app_name = todo
   
   path("detail/<int:pk>", views.details, name="detail"),
   ```

   - `detail/<int:pk>` : 특정 글의 상세 내용이므로 동적인자가 필요
   - `views.detail` : `detail`함수로 응답할 것
   - `name="detail"` : url namespace `{% url 'todo:detail' %}`

   

   path 설정을 했으니, `views.details`로 가자

   

2. views.details

   ```python
   def details(request, pk):
       return render(request, "silver/detail.html")
   ```

​		`detail` 함수는 `silver/detail.html` 을 rendering 해수는 함수

​		함수를 설정했으니 `detail.html`로 간다



​	2-1. 글의 내용을 보여줘야 하므로 더미 데이터(dummy data)로 template에 하나 만들어서 `details`가 `detail.html`을 제대로 응답하고 있는지 확인



​	3. detail.html : `base.html`을 상속받기 위해 `{% extends 'base.html' %}`을 최상단

```python
{% extends 'base.html' %}
{% block article %}

h1 detail.html

h2 제목 : 오늘의 점심은?

p 골라주세요.

{% endblock %}
```

- `base.html` : 프로젝트와 같은 레벨의 경로에 templates 폴더 생성

  `BASE_DIR / 'templates'`



4. detail 함수 정의

```
1. 상세페이지를 보고자한 글의 id 값을 가져와서

2. id 값을 기준으로 가져온 제목과 글의 내용을 보여준다.

3. id 값은 어디서 가져오는가? -> Todo.object.all()
	index.html에서 가져온다
	
4. index.html에서 요청한 id 값을 동적인자로 하여

5. 동적인자를 받아와서 해당 id를 가진 객체를 가져오는 인자로 활용 .get(pk)

6. 즉, urls => /detail/<int:pk> 의 동적인자 pk와 views => def detail(request, pk)의 매개변수 pk는 동일해야 한다(path에서 명시한 동적인자와 views 함수에서 받아오는 인자는 동일해야 한다.)

7. Todo.objects.get(pk=pk)
	pk는 todo 변수에 저장
	
8. .get(pk) 로 가져온 객체를 변수에 저장 (딕셔너리 형태)
	context = {"todo" : todo}
	return render(request, 'todo/detail.html', context)
	* context는 html에 매개변수로 전달

9. DTL 문법으로 딕셔너리 형태의 객체에서 제목(title)과 내용(content)를 `.`으로 호출
	{{todo.title}} {{todo.content}}
```

```python
def detail(request, pk):
```

```python
	todo = Todo.objects.get(pk=pk)
	context = {
	"todo" : todo
	}
```

```python
	return render(request, 'todo/detail.html', context)
```



- `.get()`메소드를 사용해서 특정 pk의 데이터를 불러온다

​	불러온 데이터를 변수에 할당(`{{ todo.title }}`, `{{ todo.content }}`)

- pk를 어떻게 받아올 것인가?

  `index.html`에서 `{% url 'posts:deatil' post.pk %}`

  <u>url 뒤에 닫는 태그 사이에</u>

  동적인자로 전달하기

- path에서도 `detail/<int:pk>` 추가



첫 번째 READ는 데이터의 목록을 출력하고,

두 번째 READ는 하나의 데이터에 대한 정보를 출력



- 정리

  내가 클릭할 component에 a태그로 링크를 걸어줍니다.

  삭제(delete)를 할 때처럼 내가 클릭한 글의 pk 값을 동적인자로 전달 받아야 한다.<br>(내가 보고싶은 글의 내용을 보고싶기 때문에)

  그 다음엔 **url**을 만들고 <br>**view** 만들고 **templates** 만들기

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

   input의 value에 

   views에서 넘겨온 {{ post.title }}과 {{ post.content }}를 각각 뿌려주기

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

