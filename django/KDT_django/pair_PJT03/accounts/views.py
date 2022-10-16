from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import UpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    # 리퀘스트 메소드가 post일 땐
    # DB에 저장한다
    if request.method == "POST":
        forms = SignupForm(request.POST)
        # 유효성 검사 진행 후 DB에 저장
        if forms.is_valid():
            forms.save()
            return render(request, "base.html")
    
    # 리퀘스트 메서드가 get 또는 유효성 검사를 통과하지 못했다면,
    else:
        forms = SignupForm()
    
    context = {
        "forms" : forms,
    }
    return render(request, "accounts/signup.html", context)

def login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')        
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

def index(request):
    # 회원 정보를 가지고 있는 유저 객체
    infos = get_user_model().objects.all()
    context = {
        "infos" : infos,
    }
    
    # 유저객체에 대한 정보를 템플릿에 출력한다.
    return render(request, "accounts/index.html", context)

# 회원 정보 조회
def detail(request, user_pk):
    # 요청으로 들어온 pk가 일치하는 유저 객체를 저장(조회하고자 하는 회원의 페이지)
    info = get_user_model().objects.get(pk=user_pk)
    context = {
        "info" : info,
    }
    return render(request, "accounts/detail.html", context)

# 회원 정보 수정
@login_required
def update(request):
    if request.method == "POST":
        forms = UpdateForm(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            # 수정이 완료되면 수정한 회원의 정보 보기 페이지로 보낸다.
            return redirect("accounts:detail", request.user.pk)
    else:
        forms = UpdateForm(instance=request.user)
    
    context = {
        "forms" : forms,
    }
    return render(request, "accounts/update.html", context)

def logout(request):
    auth_logout(request)
    return redirect("reviews:index")
