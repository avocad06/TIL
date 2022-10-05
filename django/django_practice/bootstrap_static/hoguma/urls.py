from django.urls import path
from . import views

app_name = "hoguma"

urlpatterns = [
    path("", views.index, name="index"),
    path("crate/", views.create, name="create"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
