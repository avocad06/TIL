from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# 항상 클래스 이름의 첫 글자는 대문자로
# models.Model을 통해 장고는 Post 모델이 데이터베이스에 저장되어야 한다는 것을 인식
class Post(models.Model):
    # 작성자?
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)


# 메소드를 정의?
# self의 의미가 뭐지? 호출되면 가장 첫 번째를 인자로 넣는다였던 거같은데
def published(self):
    self.pubtlished_date = timezone.now()
    self.save()


# 왜 타임존에서 할까? published_date에 바로 timezone.now()하면 안되는 건가?


# 언더바 두 개는 무슨 뜻일까?
# 던더, 더블, 언더스코어의 준말
# __str__을 호출하면 Post모델의 제목 텍스트를 반환
def __str__(self):
    return self.title
