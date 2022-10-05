from django import forms

# 장고에서 forms 모듈을 추가한다
from .models import Hoguma

# 모델폼에 적용될 모델을 가져온다.


class HogumaForm(forms.ModelForm):
    class Meta:
        model = Hoguma
        # 모델에서 form에 추가할 필드를 명시한다.
        fields = ["title", "content"]
        labels = {
            "title": "제목",
            "content": "내용",
        }
