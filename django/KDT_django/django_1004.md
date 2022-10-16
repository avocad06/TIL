장고가 하는 일(http의 핵심)

1. URL요청을 받아서
2. 처리하고
3. 응답을 해준다.

장고는 MTV패턴을 앱 별로 가지게 된다.

앱은 일반적으로 복수형으로 사용하게 되고,

앱을 생성하게 되면 앱등록을 해야 한다.

1. app 생성

2. app 등록(installed appes)

   1. 앱 단위에서 `urlpatterns`을 추가해야 runserver가 돌아간다

3. urls.py 설정

4. Index

   url을 등록하고, view 함수 생성, template 만든다.

   1. urlpatterns = [

      path('', views.index, name=index),]



게시판 만들기

CRUD를 만든다 => DB의 생성, 조회, 수정, 삭제할 수 있게 만든다는 것

UI/DB는 밀접한 관계를 가진다.

EX) 말머리를 db에 저장해놔야 UI에서도 조작을 할 수가 있는 것(`기능`)



왜 상속을 받나요?

​	설계는 해놓되 기능자체는 상속 받아서 쓰고 싶어서.

`python manage.py show migrations` : DB에 반영되었는지 확인(조회)도 가능하다.

CRUD 기능 구현

create

​	핵심 :  기능별 url에 매핑되는 view함수는 1개씩이어야 한다. 하나의 url을 두 개의 view함수로 처리할 수 없다.

​				특정 url에 대응되는 기능은 각각이므로.



사용자에게 HTML Form 을 제공, 입력한 데이터를 처리

1. HTML Form 제공

   1. `new/`에서 `views.new` 함수를 처리할 것

      path('new/', views.new, name=new),

   2. def new(request):

      return render(request, 'articles/new.html')

   3. new.html

      form : 사용자에게 양식을 제공하고 값을 받아서(input : name, value) 서버에 전송(action)

2. 입력받은 데이터 처리

   1. `create/`에서 `views.create` 함수를 처리할 것

      path()

`POST` : 서버에 변화를 야기시킨다. form을 통해서 제출할 때는 POST 메서드를 쓰자

POST 요청은 요청 메시지 상에 담겨서 전달된다.(url 안에 담기는 게 아니라)



# Django ModelForm

> 모델과 폼은 긴밀한 관계

UI는 우리의 데이터베이스(DB)와 밀접한 관계를 가지게 되어있다.

- 사용자로부터 값을 받아 데이터베이스에 저장하여 활용하기 때문이다.

- 모델에 정의한 필드의 구성 및 종류에 따라 HTML Form이 결정된다.

사용자가 입력한 값이 DB의 데이터 형식과 일치하는지 확인하는 `유효성 검증`이 반드시 필요하다.

서버 쪽에서 검증하는 로직을 추가해야 한다. => ModelForm 의 등장



`forms.py`

```
from django import forms
from .models import Ariticle

class AricleForm(forms.ModelForm):
	
	class Meta:
		model = Article
		field = '__all__'
# 아티클 모델에 있는 모든 필드를 가져와서 쓰겠다.
# 기존에 있는 모든 폼을 대체해서 사용하기(인풋 라벨 이런 거 다)
```

```
article_form = AritlceForm()
context = {
	'article_form' : article_form
}
return render(request, 'articles/new.html', context=context)
```

ArticleForm(request.POST)

request.POST해 온 것을 그대로 넘겨준다는 의미



## 상세보기

특정한 글을 본다. => <u>variable routing이 필수이다.</u>

DB에 있는 PK를 url에 넣어주어야 한다.

path('<int:pk>/', views.detail, name='detail'),

views.py

def detail(request, pk):

article = Article.objects.get(pk=pk)

context = {

'article' : article

}

return render(request, 'articles/detail.html', context)

detail.html

{{ article.pk }}

{{ article.created_at }} | {{ article.updated_at }}

{{ article.content }}

index.html

{% url 'articles:detail' article.pk%}



## 수정하기

특정한 글을 수정한다 => 사용자에게 수정된 글을 받아서 특정한 글을 수정한다.

사용자에게 수정할 수 있는 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

`<int:pk>/update`

1. 수정을 할 수 있도록 `path('<int:pk>/update/', views.update, nmae='update')`

​	detail에서 a태그로 이동할 수 있는 버튼{% url 'article:update' article.pk %}을 만든다.

2. def update(requet, pk):

   // GET : Form을 제공

   article_form = ArticleForm()

   context = {

   'article_form': article_form}

   return render(request, 'articles/update.html', context)

   

instance=article 을 넣어줘야 <u>있던 값</u>을 수정이 가능하다.

Create 1. ui 제공 2. db저장

Read 1. DB에서 특정 가져와서 조회

Delete 1. DB에서 특정 가져와서 삭제

Update 1. UI제공 2. DB 저장

ModelForm은 모델에 정의된 필드대로 UI를 그려주고, 유효성 검사를 하고, DB에 저장까지 해준다.

요청에 따라 다른 일을 하게 하면서 같은 VIEW함수에서 (동일한 URL에서) 처리가 가능해진다.

POST요청이 왔지만 FORM으로 돌아가게 하기 위해서 메소드의 분리와 뷰함수의 일원화



# 들여쓰기의 중요성

```python
def create(request):
    if request.method == "GET":
        article_form = ArticleForms()
        context = {"form": article_form}

    elif request.method == "POST":
        # title = request.POST.get("title")
        # Article.objects.create(title=title)
        article_form = ArticleForms(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("normal:index")

    return render(request, "normal/create.html", context)
```

request가 POST요청으로 들어오면 모델폼에 매개변수로 request.POST값을 전달한다.

브라우저에서 입력된 POST값이 모델폼에 유효한 경우 폼 내용을 DB에 반영한다.(`article_form.save()`)

DB에 반영이 성공적으로 되었으면 index 페이지로 돌아간다.(`normal:index`)

request가 POST 요청이 아니라면 브라우저가 요청한 form을 보여준다.(`article_form = ArticleFroms()` 이후 context 값으로 보내주기)

여기서 들여쓰기가 중요한데, `context = {"form" : article_form}` 은 1. request가 GET이거나, 2. request가 POST이지만 모델폼에 유효하지 않은 경우 둘 다를 처리해야 한다.