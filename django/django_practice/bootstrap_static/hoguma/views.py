from django.shortcuts import render, redirect
from .models import Hoguma
from .forms import HogumaForm

# Create your views here.
def index(request):
    articles = Hoguma.objects.all()
    forms = HogumaForm()
    context = {
        "articles": articles,
        "form": forms,
    }
    return render(request, "hoguma/index.html", context)


# def create(request):
# create는 두 가지 경우로 나눌 수가 있다.
# form을 요청하는 경우(GET)와
# form에 저장하는 경우(POST)
# 하지만 모달을 사용하는 경우이므로 이 두 경우를 따로 보고,
# create에 대한 요청은 POST일 때만 요청된다고 생각한다.
def create(request):
    if request.method == "POST":
        form = HogumaForm(request.POST)
        # 폼이 유효하다면
        if form.is_valid:
            form.save()
            return redirect("hoguma:index")
        # 유효하지 않다면?
        # 모달에서 처리할 때는 유효하지 않을 때 유효성 메시지를 띄워주고
        # 아무런 페이지 처리가 일어나지 않는다.


def detail(request, pk):
    details = Hoguma.objects.get(pk=pk)
    form = HogumaForm(instance=details)
    form.fields["title"].disabled = True
    form.fields["content"].disabled = True
    context = {
        "article": details,
        "form": form,
    }
    return render(request, "hoguma/detail.html", context)


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


def delete(request, pk):
    content = Hoguma.objects.get(pk=pk)
    content.delete()
    return redirect("hoguma:index")
