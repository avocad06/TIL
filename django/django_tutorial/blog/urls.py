from django.urls import path
from . import views

urlpatterns = [
    # 루트 url
    # http://127.0.0.1:8000/ 주소로 들어오면 views.post_list를 출력할 것
    # url name sapcing 으로 뷰를 식별(url에 이름붙이기)
    # 어떤 앱이든 하나라도 view가 설정되지 않으면 다른 웹페이지도 다 실행이 안 된다.
    path("", views.post_list, name="post_list"),
]
