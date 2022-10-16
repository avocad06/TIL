1. 브랜치를 새로 생성한다.
2. 새로 만든 브랜치에서 생성



```
회원정보수정
1. url : path("accounts/update/<int:user_pk>", views.update, name="update")
```

회원정보 수정을하는데, <u>로그인한 유저</u>의 정보를 수정하려면?

```
url : path("accounts/update/", views.update, name="update")
```

기능(views)

`GET` : Form 요청(제공)

`POST` : 실제 수정



```
def update(request) : 
if request.method == "POST":
	
else:
	form = 
	context = {
	'form' : form,
	}
	return render(request, "acounts/update.html', cotnext")
```



3. 어느 정도 진행이 됐으면 새로운 브랜치에서 commit