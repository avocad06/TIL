from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("movies/", views.movies, name="movies"),
    path("movies/<int:pk>", views.content, name="content"),
    path("movies/create/", views.create, name="create"),
    # path("movies/<int:pk>/update/", views.update, name="update"),
    # path("movies/<int:pk>/delete", views.delete, name="delete"),
]
