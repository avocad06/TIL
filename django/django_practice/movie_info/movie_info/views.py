from django.shortcuts import render, redirect
from .models import Movie
from .forms import InfoForm

# Create your views here.
def movies(request):
    inform = Movie.objects.all()
    context = {
        "titles" : inform
    }
    return render(request, "movie_info/movies.html", context)


def create(request):
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:movies")
    else:
        form = InfoForm()
    context = {
        "form": form,
    } 
    return render(request, "movie_info/create.html", context)

def content(request, pk):
    return render(request, "movie_info/content.html")