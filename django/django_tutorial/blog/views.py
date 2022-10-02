from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )

    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_new(request):
    if request.method == "POST":
        # 만약 method가 POST라면,
        #  폼에서 받은 데이터를 PostForm에 넘겨준다
        form = PostForm(request.POST)

        # 폼이 유효하면
        if form.is_valid():
            post = form.save(commit=False)
            # 현재 사용자를 나타내는 모든 요청에 대한 속성을 제공
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            # 작성하고 제대로 작성됐는지 페이지 보여주기
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})
