from django.urls import path
from . import views

app_name = "hoguma"

urlpatterns = [
    path("", views.index, name="index"),
    path("crate/", views.create, name="create"),
]
