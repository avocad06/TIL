# Django Message Framework

> 10월 17일자 복습

[참고 : Django-framework-알아보기](https://ssungkang.tistory.com/entry/Djangomessage-framework-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)

로그인에 성공했을 때, 혹은 실패했을 때 다른 알람을 1회성으로 띄워준다. Message Framework는 <u>1회성 메시지</u>를 담는 용도로 사용한다. (HttpRequest 인스턴스를 통해 남기기 때문에) <u>새로고침하면 사라진다.</u>

## Message level

- `DEBUG`

- `INFO`

- `SUCCESS`

- `WARTNING`

- `ERROR`

  

## Configuring the message engine

1. 백엔드를 정해야 한다.(`settings.py` 하단에 아래 문장 추가)

```python
# Message Framework
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
```

## Using messages in views and templates

1. Adding a message `views.py`

   > 파이썬 코드는 무조건 `views.py`

   ```python
   from django.contrib import messages
   messages.add_message(request, messages.INFO, 'Hello world.')
   ```
   

2. 원하는 메시지 추가

   > 메시지를 보고자 하는 함수에 각각 추가

   ```python
   messages.success(request, 'Profile details updated.')
   ```

   메시지 내용을 수정할 수 있다.

   ```python
   messages.success(request, '글 작성이 완료되었습니다.')
   ```

3. Displaying messages `base.html`

   > **In your template**, use something like:
   >
   > <u>`context` 설정 없이도 템플릿 변수로 사용할 수 있다.</u> => `settings.py`에서 정의돼 있음.

   ```html
   {% if messages %}
   <ul class="messages">
       {% for message in messages %}
       <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
       {% endfor %}
   </ul>
   {% endif %}
   ```

   `tags` : message의 level 출력

   `message` : message의 내용 출력

   

4. 결과 : 순서가 없는 리스트의 형태로 메시지 출력



## 출력되는 메시지에 부트스트랩 클래스 주기

```html
  {% if messages %}
    {% for message in messages %}
      <div class="alert alert-{{ message.tags }}">
        {{ message }}
      </div>
    {% endfor %}
  {% endif %}
```

`views.py`에서 정한 메시지 태그가 상황에 따라 {{`message.tags }}`에 담기면서 부트스트랩 클래스가 적용

> 메시지 태그와 부트스트랩의 클래스가 일치할 때만 가능<br> `danger`라는 메시지 태그가 없으므로 부트스트랩이 적용되지 않음.

```
alert-success
```

```
alert-warning
```

