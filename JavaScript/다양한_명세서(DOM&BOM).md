```
⚡ 요약 ⚡
1. DOM 명세서(웹페이지 내의 모든 컨텐츠를 객체로 제공)
"문서 구조, 조작, 이벤트"에 관한 설명
https://dom.spec.whatwg.org

2. CSSOM 명세서
스타일시트와 스타일규칙, 이 둘을 어떻게 조작할 수 있는지, 이 둘과 문서 사이의 관계를 어떻게 조작할 수 있는지에 대한 설명
https://www.w3.org/TR/cssom-1/

3. HTML 명세서
태그 등의 html 언어, setTimeout(), alert, location 등의 다양한 브라우저 기능을 정의한 BOM에 대한 설명
DOM 명세서에 다양한 프로퍼티와 메서드를 추가해 확장한 명세서
https://html.spec.whatwg.org
```



- 자바스크립트 : 본래 웹 브라우저에서 사용하려고 만든 언어

호스트 (자바스크립트가 돌아가는 플랫폼, *브라우저, 웹서버* 등이 해당) 환경은 플랫폼에 특정되는 객체과 함수를 제공

- 웹브라우저 : 웹페이지를 제어하기 위한 수단 제공
- Node.js : 서버 사이드 기능을 제공



## 호스트 환경이 웹브라우저일 때

- 최상단 : '루트' 객체 `window`***객체***
  1. **전역 객체**
  2. 브라우저 창을 대변하고, 이를 제어할 수 있는 메서드를 제공

​	전역 함수는 전역 객체(window)의 메서드

- `window` 객체의 하위는 `DOM`, `BOM`, `JavaScript`가 있다.



### 문서 객체 모델(DOM, Document Object Model)

> 문서 객체 모델 `document`
>
> <u>*웹페이지내의 모든 컨텐츠를 객체로*</u> 나타내줌
>
> 해당 객체는 수정이 가능

- `document` 객체는 페이지의 기본 '진입점' 역할을 한다.

- `document` 객체를 이용해 페이지 내의 무엇이든 변경할 수 있고, 원하는 것을 만들수도 있다.

- DOM은 서버사이드 스크립트에서도 사용한다.

- 스타일링을 위한 CSS 객체모델 CSSOM도 있지만, 실무에서 자주 접하지는 않는다.



### 브라우저 객체 모델(BOM, Brower Object Model)

> 문서 이외의 모든 것을 제어하기 위함
>
> 호스트환경이 제공하는 *추가 객체*

- `navigator` 객체 : 브라우저와 운영체제에 대한 정보를 제공

  현재 사용중인 정보 브라우저 정보

  ```javascript
  navigator.userAgent
  
  // 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
  ```

  브라우저가 실행중인 운영체제 정보

  ```javascript
  navigator.platform
  
  // 'Win32'
  ```

  

- `location` 객체 : <u>현재 URL을 읽을 수 있게 해주고,</u> 새로운 URL로 변경(redirect)할 수 있게 함.

  현재 URL

  ```javascript
  location.href
  
  'https://ko.javascript.info/browser-environment#ref-2035'
  ```

  새로운 URL 변경

  ```javascript
  if (confirm("위키피디아 페이지로 가시겠습니까?")) {
    location.href = "https://wikipedia.org"; // 새로운 페이지로 넘어감
  }
  ```

  