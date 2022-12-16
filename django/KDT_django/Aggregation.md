# Aggregation

> django쿼리를 사용하여 집계 값을 생성하고 반환하는 방법



Aggregate와 annotate()는 둘 다 객체의 요약값을 정의한다.

`Aggregation`은 한 테이블의 모든 객체를 통틀어서 집계한 요약 값을 계산하여 이름-값 쌍의 딕셔너리로 반환한다.

```python
# 모든 책들 중에서 가장 비싼 책의 가격
Book.objects.aggregate(Max('price'))
>>> {'price__max':34.35}
```



`annotate`는 객체 하나하나마다 요약 값에 대한 주석 필드를 추가한다. *쿼리셋을* 반환하기 때문에 `order_by()`, `filter()`, 다른 `annotate()`절까지 추가할 수 있다.

```python
# 각 게시물의 좋아요 수
Article.objects.annotate(Count('like_users'))
```

 

## Agregate

`aggregate`로 객체에 대한 요약된 값을 구할 수 있다.

```django
from django.db.models import Avg
Book.objects.all().aggregate(Avg('price'))
{'price__avg' : 34.35}
```

all()은 생략할 수 있으므로

```django
Book.objects.aggregate(Avg('price'))
```

로 작성해도 결과는 같다.





aggregate절의 인자는 계산하려는 집계 값을 설명한다.

> 사용 가능한 *집계 함수* 목록은  [쿼리셋 api]('https://docs.djangoproject.com/en/4.1/ref/models/querysets/#aggregation-functions')에서 참고할 수 있다.

- aggregate절은 이름-값 쌍의 딕셔너리를 반환한다. 이름은 집계 값의 식별자이다.
- 이름은 필드 이름과 집계 함수에서 자동으로 생성된다.

```python
# 좋아요 누른 유저 중 pk 값이 가장 높은 사람
>>> Article.objects.aggregate(Max('like_users'))
{'like_users__max': 9}
```

​	필드이름 : `like_users`

​	집계 함수 : `Max()`

​	자동 생성 : `like_users__max`



별칭을 정의할 수도 있다.

```python
>>> Article.objects.aggregate(highest__pk=Max('like_users'))
{'highest__pk': 9}
```



둘 이상의 집계가 필요하다면, 인자를 추가하면 된다.

```python
# 좋아요 누른 사람 중 가장 높은 pk와 낮은 pk
>>> Article.objects.aggregate(hightest__pk=Max('like_users'), lowst__pk=Min('like_users'))
{'hightest__pk': 9, 'lowst__pk': 4}
```



