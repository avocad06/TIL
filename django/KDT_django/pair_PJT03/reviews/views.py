from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Review
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def create(request):
    if request.method == "POST":
        
        forms = PostForm(request.POST)
        # 사용자가 입력한 값이 유효성을 통과하면 DB에 저장한다.
        if forms.is_valid():
            forms.save()
            # 게시글 작성 후 제대로 작성됐는지 확인하도록 게시글 상세보기 페이지로 보낸다.
            pk = Review.objects.order_by("-pk")[0].pk
            return redirect("reviews:detail", pk)
        
    # request.method 가 GET일 경우
    else:
        # 빈 폼
        forms = PostForm()
    context = {
        "forms" : forms,
    }
    return render(request, "reviews/create.html", context)

def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews" : reviews,
    }
    return render(request, "reviews/index.html", context)

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        "review" : review,
    }
    return render(request, "reviews/detail.html", context)

@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    # 요청이 POST로 들어온다면
    if request.method == "POST":
        forms = PostForm(request.POST, instance=review)
        if forms.is_valid():
            forms.save()
            # 수정 후 디테일 페이지로 돌아간다.
            return redirect('reviews:detail', review_pk)
    # 요청이 GET이라면
    else:
        # 사용자가 이전에 입력한 값만 있는 폼을 보여준다.
        forms = PostForm(instance=review)
    context = {
        "forms" : forms,
    }
    return render(request, "reviews/update.html", context)

@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('reviews:index')
    