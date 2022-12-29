```powershell
npx create-react-app 프로젝트 이름
```

```
npx create-react-app reactexam-01
```

 3분 - 5분 정도 소요



reactexam-01 폴더 생성

(폴더명과 프로젝트명이 동일하다면, 잘라내기 해서 가장 최상단의 폴더로 붙여넣기 => 폴더명이 루트 폴더가 됨)

package.json > react가 설치돼있는 것을 확인

scripts : 명령어의 shorcut 느낌

```powershell
npm start
```

```powershell
You can now view reactexam-01 in the browser.
```

리액트 실행 (localhost:3000)

종료 : `Ctrl` + `c`



`App.js`

funcion App() 은 html을 return 한다.

```
src/App.js를 수정하고 저장해서 reload해라
```



어떻게 js만으로 html이 랜더링될까?

=> 함수 App() 이 return 하는 html들이 id가 root인 div의 자식요소로 들어감.



```javascript
import App from './App';
```

App.js에서 함수 App()을 불러와서

```javascript
const root = ReactDom.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

 App()이 반환하는 값을 id 가 root인 요소 아래 자식 요소로 render한다.

id값이 root인 요소는 어디에서 왔을까?

=> `public`의 `index.html`에 위치한다.



`node_modules` : 외부 모듈을 저장하고 있는 폴더(리액트도 외부 모듈임)

용량이 굉장히 크기 때문에 github에 올리려면 제외할 것

node_modules가 삭제돼도 packate-lock.json에 어떤 모듈이 필요한지 명시되어 있기 때문에 node_modules가 없다면 npm i 명령어로 설치하면 됨.

```powershell
npm i
// npm install
```



`public` : favicon, index.html, robots.txt(구글 써치봇 수집 관련) 가 위치한 폴더



- 불필요한 파일 삭제

`src/`

`test`가 들어가는 폴더들은 삭제(App, setup)

App.test.js

setupTests.js

`logo.svg`

`Vitals`가 들어가는 폴더들 삭제 후 import 되는 부분들 코드 삭제

reportWebVitals.js



`App.js`

App() 안에서 변수를 선언하고 해당 변수를 return하는 html에서 `{}`를 활용하여 템플릿 리터럴처럼 사용할 수 있음.(표현식도 쓸 수 있지만 반환값이 문자열이나 숫자여야만 함. boolean 등은 x)

js와 html을 합쳐서 사용할 수 있는 문법 = js 표현식 = java script expression = JSX



컴포넌트 방식

별도의 html 요소를 묶어서 모듈처럼 만들고 내보내서 다른 파일에서 쓸 수 있게 하는 방식



App을 내보내서

`export default App;`

다른 파일에 import from 경로 로 사용할 수 있음.

`export default`는 1개만 내보낼 수 있음.



jsx의 컴포넌트는 무조건 return해야 함.



`index.js`에서는 최상위 컴포넌트를 정의할 수 있다.

root div의 자식요소로 들어가는 컴포넌트(=App)를 정의하는 곳이기 때문에.

(이름은 변경할 수 있음. 관례상 최상위 컴포넌트를 App이라고 부른다.)



JSX 문법 규칙

1. 닫힘 규칙 : 무조건 닫는 태그는 있어야 한다.

   ```javascript
   </div> <img /> 셀프클로징 태그
   ```

2. 최상위 태그 규칙

   ```
   JSX expressions must have one parent element.
   ```

   JSX로 컴포넌트를 만들어서 return하려면 최상위태그로 다른 모든 태그를 묶어야 함.

   안 묶고 싶다면? => react.fragment

   ```
   import React from 'react';
   ```

   ```
   <React.Fragment></React.Fragment>
   ```

   ```
   <> 빈 태그도 가능!
   ```

3. css

   ```react
   className="App"
   ```

   ```
   import "./App.css";
   ```



이렇게 하면 안 되나? (`index.js`에 바로 component import 하기)

![image-20221229181448850](assets/image-20221229181448850.png)



# State(상태)

+ 버튼을 누르면 H2 태그 사이에 있는 숫자가 증가/감소하기를 원함.

+ H2 사이에 있는 숫자만 동적으로 변하면 됨. = 숫자가 상태다.

  기본값이 0에서 출발하고

  1씩 증가하고

  1씩 감소하는

  count 숫자의 상태



count 숫자를 **상태**로 만들어주기 위해 `useState` 메서드를 추가적으로 import

```react
import React, {useState} 'from' 'react';
```



```javascript
const [count, setCount] = useState(0);
```

리액트 메서드 `useState`는 배열을 반환하고, 배열의 비구조화 할당을 통해 



count 상태가 바뀔 때마다 Counter컴포넌트는 return을 다시 한다 = re render

컴포넌트는 자신이 가진 state가 변화하면 화면을 다시 그린다. = 함수가 다시 호출된다. = re render

컴포넌트 별로 독립적인 랜더링이 이루어진다.



컴포넌트는 state를 두 개 가져도 상관이 없다.

state를 활용하면 화면에 나타나는 데이터를 쉽게 교체하고 업데이트할 수 있다.