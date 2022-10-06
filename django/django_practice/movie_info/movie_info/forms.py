from django import forms
from .models import Movie

class InfoForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = "__all__"
        labels = {
            "title" : "제목",
            "summary" : "줄거리",
            "running_time" : "상영 시간",
        }