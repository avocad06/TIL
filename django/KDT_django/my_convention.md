1. 스타트 프로젝트

2. 프로젝트 했으면 앱을 등록해야지(겸사겸사 settings 에서 언어랑 타임존 설정도 해주자)

   ```python
   ko-kr
   Asia/Seoul
   ```

3. 앱을 등록했으면 프로젝트 폴더의 `urls.py`에서 앱urls에 대한 요청을 관리하자

4. include로 해주자. index는 루트페이지로 설정하자.

5. 프로젝트 url 설정했으면 hoguma로 넘어가서 앱 url 설정해주자.

   1. 앱 url에서 중요한 것은 urlpatterns이다.
   2. app_name과 url은 부차적인 것

6. url 설정했으면 해당 url을 처리할 views로 이동해주자

   1. 함수를 정의할 때는 먼저 이 함수는 어떤 요청을 어떻게 처리하는 함수인지 정할 것
   2. index는 index template을 보여주는 함수이다.
   3. 필요한 것: 'index.html'을 render 하겠다(render() 함수 호출)
      1. 이때 index.html은 어디에 있지? hoguma/tmplates/hoguma에 있을 예정이니까
      2. 'hoguma/index.html'을 response해 주어야 한다.

7. 우선 template을 만들자

   1. 상속 받을 'base.html' 먼저 생성해보자

      1. 프로젝트와 같은 레벨의 폴더에 존재해야 하므로 templates 폴더 생성 후 'base.html' 파일 생성

         중요! 'base.html'에서도 `{% block content %} {% endblock %}`을 설정해야 한다.

         ​	모든 템플릿을 상속 받은 거와 똑같이하지 않을 거니까(개별 달라지는 부분이 block 안에 들어가야 하니까)

      2. 생성했으면 경로 설정 해줘야지

         1. settings.py 에서 templates 에 BASE_DIR/'templates' 추가해준다.

   2. base.html 생성했으면 hoguma/templates/hoguma/index.html 만들어서 제대로 상속받는지 확인하자

   3. 잘 작동한다면 url 요청에 대해 html을 잘 응답하고 있는 것이므로 views로 이동해서 세부 동작을 정해보자.

8. 다시, view

   1. index.html의 역할은 작성된 게시물을 조회해주는 역할이다.

      1. 작성된 결과물은 데이터베이스에 저장이 되어 있어야 한다.
         1. 모델링 했는가?
         2. 안했음. => models 가서 마이그레이션 하러 가자.

   2. 모델링은 models.Model 클래스를 상속받아서 한다.

      1. 모델링은 설계에 따라 달라질 수 있다.

      2. 모델링이 되었으면 makemigrations migrate 해준다.

      3. 만약, 속성이 아니라 메소드가 수정되면 migrate만 해주면된다.

         1. makemigrations할 때마다 initial 파일이 생성되는데 10번까지도 가봤다.
         2. 메소드 수정은 수정으로 안 보는 것 같다. migrate하면 적용되니까 매번 새로 migration폴더 만들지 말고 migrate하자.

      4. 데이터베이스에 제대로 들어갔는지 확인

         1. db.sqlite3 에서 open database 해서 확인해보거나

         2. `$ python manage.py showmigrations` 해서 확인할 수 있다.

            ```python
            hoguma
             [X] 0001_initial
            ```

   3. 모델링이 되었으면 다시 views로 돌아가서 할 일을 하자.

      1. 우리가 할 일은 루트페이지(name=index)에서 전체 목록을 보여줘야 한다.

      2. 우선 DB에서 값을 가져와야 하므로 맨 상단에 모델링한 `Hoguma` 모델을 import 해야 한다.

         ```python
         from .models import Hoguma
         ```

      3. 그리고 가져온 DB값을 템플릿에서 보여줘야 하므로 context로 넘겨준다.

         1. return render함수의 유사 딕셔너리 형태의 세번째 인자이다.

            ```python
            def index(request):
                articles = Hoguma.objects.all()
                context = {"articles": articles}
                return render(request, "hoguma/index.html", context)
            ```

         

9. context로 넘겨주었으니 다시 templates로 돌아가서 가져온 DB값을 보여주자.
   1. 템플릿에서 중요한 것은 어떤 내용을 브라우저에서 보여줄 지이다.
      1. 우리가 보여줄 것은 제목, 작성시간, 수정시간이다.
      2. 제목을 누르면 상세 페이지로 이동하게 할 것이고,
      3. 테이블의 형태로 보여주고자 한다.
      4. 모든 사용자의 글을 보여주어야 하므로 가져온 객체를 하나씩 꺼내서 보여주자.(for문 적용)

10. 근데 아직 만들어진 글이 없어서 아무것도 안 보이네. create기능을 만들자.

11. 새 글 쓰기 기능은 루트페이지에서 이동가능하도록 링크(버튼)을 만들어준다.

    1. 루트페이지에서 버튼 추가
    2. 이때 버튼의 이동 링크는 네이밍할 url로 지정해놓고 새로운 요청 url이 생겼으니 url로 가서 path를 추가해준다.(주문서 추가)

12. urls 에서 path추가하기

    1. `crate/` 라는 url 요청이 들어오면 `create`함수를 실행시킬 것이다.(url 네임은 `create`)

       ```python
       path("create/", views.create, name="crate"),
       ```

13. path 추가했으니 path에서 추가한 views 함수로 이동하자

    `crate`함수는 새로운 request 객체를 받았을 때, 그것을 DB에 추가하는 역할을 한다.

    객체를 생성하는 sql orm 명령어는  `.objects.create()`이다.

    이때, request객체를 받아오기 위해(브라우저, 사용자로부터 입력값을 받아오기 위해) templates에서 form태그를 활용하는데,

    1. html 폼 태그를 활용할 것인지

    2. django ModelForm 클래스를 상속받아 활용할 것인지

       나뉘게 된다. 여기서는 ModelForm 로직으로 처리해보자.

14. ModelForm 클래스를 생성하려면 `forms.py` 파일이 앱 내에 있어야 한다. ( 이 순서는 CRUD 진입 전에 해도 상관 없다. 이왕이면 진입 전에 진행하는 거로 하자.)

    ```python
    from django import forms
    from .models import Hoguma
    
    
    class HogumaForm(forms.ModelForm):
        class Meta:
            model = Hoguma
            fields = ["title", "content"]
    ```

    폼 레이블은 딕셔너리 형태로 정의한다.

    ```python
            labels = {
                "title": "제목",
                "content": "내용",
            }
    ```

15. 다시 views로 돌아가서 form을 템플릿에 보내주자

    ```python
    from .forms import HogumaForm
    ```

    ```python
    context = {
            "articles": articles,
            "form": forms,
        }
        return render(request, "hoguma/index.html", context)
    ```

16. 템플릿에서 form 은 보안을 위해 `{% csrf_token %}` 과 `{% context로 보내준 form 이름 %}`을 추가한다. 이때 부트스트랩 form을 적용시키고 싶다면 사전 설정(pip install, settings 설정, `{% load bootstrap5 %}`) 모두 하고 `{% *bootstrap_form* form %}` 처럼 form 이름 앞에 bootstrap 명령어만 적어주면 된다.

17. 정상적으로 폼이 새 글 입력 페이지에 출력되는 것을 확인했으면, 다음은 detail 뷰로 넘어가자.

18. detail 뷰는 목록에서 제목을 클릭하면 이동할 수 있도록 한다.

    1. 템플릿에서 detail뷰를 요청하는 링크(버튼)을 생성한다.

19. 요청 url이 새로 추가 되었으므로 다시 url로 돌아가서 path를 추가한다.

    ```python
    path("detail/<int:pk>", views.detail, name="detail"),
    ```

20. detail 페이지에 대한 요청을 처리할 view 함수 detail을 정의 한다.

    1. detail 함수는 상세페이지를 보여주는 함수이다.(pk 가 인자로 들어온다)

    2. 요청받은 pk와 pk가 같은 DB의 정보를 보여주어야 하므로 context를 넘겨주어야 한다.

    3. ModelForm과 같은 형태로 템플릿에 보내보자.

    4. 같은 형태로 템플릿에 보내는 경우, context로 받아온 ModelForm의 속성이 Form이기 때문에 상세 보기 페이지임에도 수정이 가능해지는 상황이 발생한다.

       ```python
           form.fields["title"].disabled = True
           form.fields["content"].disabled = True
       ```

       위 코드를 `detail` 함수에 추가하면 브라우저에 입력 폼과 같은 형태를 출력하되 사용자로부터 입력값을 받지 않게 할 수 있다.

21. detail 뷰에서 수정하기 버튼(링크)을 누르면 수정하기로 이동할 수 있게 한다.

    1. 링크가 요청하는 url은 편집이 가능한 페이지이다. 새로운 기능이 추가 되었으므로 이를 요청할 url을 추가한다.

22. path에서 편집하기 요청 url 만들기

    특정 글을 편집하는 기능이므로 특정 글의 동적 인자를 필요로 한다.

    ```python
    path("edit/<int:pk>", views.edit, name="edit"),
    ```

23. 새로운 요청 url이 생성되었으므로 이를 처리할 view 함수를 정의한다.

    1. `edit`함수는 request요청 방식에 따라 두 가지를 처리하는 함수이다.
    2. GET방식으로 요청되었을 때 브라우저에 기존값이 존재하는 form을 출력하고,
    3. POST방식으로 요청되면 유효성 검사 후 사용자가 입력한 form의 값을 DB에 저장한다.
    4. 메소드를 분기하고, 각 요청에 대해 어떻게 응답할지 정하자.
    5. form 을 보여주는 html을 출력하려면 rendering 하여 응답을 해야하고,
    6. form으로부터 입력 받은 값을 저장한 후 수정된 내용이 보고 싶다면 detail 뷰로 redirect 해야 한다. 이때, 만약 입력받은 값이 유효하지 않으면 템플릿으로 보낸 form의 에러메시지가 자동으로 처리된다. 이때의 응답 또한 rendering이어야 한다.

    ```python
    def edit(request, pk):
        content = Hoguma.objects.get(pk=pk)
        if request.method == "POST":
            form = HogumaForm(request.POST, instance=content)
            if form.is_valid():
                form.save()
                return redirect("hoguma:detail", pk)
        else:
            form = HogumaForm(instance=content)
        context = {
            "form": form,
            "article": content,
        }
        return render(request, "hoguma/edit.html", context)
    ```

24. view 함수를 정의하였으므로 template으로 넘어가서 `edit/<int:pk>` 가 GET방식으로 요청될 때 출력할 html을 생성한다. (`edit.html`)

    1. form에 입력된 값을 저장해야 하므로 form의 메서드는 `POST`로 명시를 해준다.

    2. submit이 있어야 요청이 되므로 꼭 만들어줘야 한다.

       ```python
       <input type="submit" class="btn btn-outline-dark" value="저장하기">
       ```

25. 편집이 정상적으로 되는 것을 확인 했으면 삭제 기능을 요청할 url을 생성한다. 삭제 기능은 detail뷰의 링크(버튼)으로 요청한다.

26. 새로운 기능에 대한 요청이 발생했으므로 urls에 삭제 기능에 대한 주문 url를 추가한다. 특정 글을 삭제하는 것이므로 동적 파라미터가 필요하다.

    ```python
    path("delete/<int:pk>", views.delete, name="delete"),
    ```

27. `delete/<int:pk>` 요청을 처리할 views함수를 만들어준다.

    1. delete 함수는 특정 글에 대한 삭제 기능을 한다.
    2. 요청 url로 받은 pk 인자와 DB에서 그 인자가 일치하는 객체를 찾아서
    3. 삭제해야 한다.(`.object.delete()`)
    4. 삭제 후 루트 페이지로 돌아간다.

    ```python
    def delete(request, pk):
        content = Hoguma.objects.get(pk=pk)
        content.delete()
        return redirect("hoguma:index")
    ```

    