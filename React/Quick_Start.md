![Quick_Start](assets/Quick_Start.gif)

# Quick Start

> 컴포넌트를 만들고 중첩하는 방법
>
> 데이터를 화면에 보여주는 방법
>
> 이벤트 대응과 화면을 업데이트하는 방법
>
> 컴포넌트간 데이터를 주고받는 방법

## Creating and nesting components

컴포넌트는 작게는 버튼 하나일수도 있고, 크게는 페이지 전체가 될 수도 있다.

**리액트의 컴포넌트는 마크업을 반환하는 자바스크립트 함수이다.**

```react
function MyButton() {
    return (
    <button>I'm a button</button>)
}
```

`<MyButton>`컴포넌트를 선언했으므로 다른 컴포넌트에 중첩시킬 수 있다.

⚠ 컴포넌트는 대문자로 시작해야 한다.(HTML태그는 소문자여야 한다.)

```
React component names must always start with a capital letter
```

`App.js`

```react
function MyButton () {
    return (
    <button>I'm a button</button>)
}

export default function MyApp() {
    return (
    <div>
            <h1>Welcome to my app</h1>
        </div>)
}
```

`export default`는 파일의 주요 구성 요소를 지정한다.

리액트에서 사용하는 마크업 문법을 JSX라고 한다. 

JSX는 HTML보다 엄격하기 때문에 닫는 태그가 꼭 필요하다.(`<br>`같은 안닫히는 HTML태그도 `<br/>`처럼 닫아줘야 한다.)

컴포넌트는 여러 개의 JSX태그를 반환할 수 없기 때문에, 하나의 태그로 꼭 묶어줘야 한다.

[transform : HTML을 올바른 JSX문법으로 바꿔주는 온라인 툴](https://transform.tools/html-to-jsx)

```react
function AboutPage() {
    return (
    <>
        <h1>About</h1>
        <p>Hello there.<br/>How do you do?</p>
        </>)
}
```

리액트에서는 HTML의 `class` 속성을 `className`으로 표기한다.

JSX를 사용하면 마크업을 JavaScript에 넣을 수 있고, 중괄호(`{ }`)를 사용하면 JavaScript로 탈출할 수 있다.(escape back) = JSX에서 JavaScript 표현식, 변수를 사용하고 싶으면 중괄호를 사용한다.

이항연산자와 변수를 연결하는 문자열 연결도 사용 가능하다.

```react
const user = {
    name: 'Hedy Lamarr',
    imageUrl: 'https://sjeikkjiemkjt',
    imageSize: 90,
}
```

`user` 라는 이름의 객체가 있을 때

```react
export default function Profile() {
    return (
    <>
      <h1>{user.name}</h1>  
      <img
          className="avatar"
          src={user.imageUrl}
          alt={'Pthoo of' + user.name}
          style={{
                width: user.imageSize,
                height: user.imageSize
            }}/>
    <>)
}
```

처럼 컴포넌트를 선언할 수 있다.

스타일 속성이 JavaScript 변수에 의존하는 경우 `style={{}}`속성을 사용할 수 있다. = 인라인 속성은 `style={{margintTop: 50px,}}` 이런 식으로 객체를 넣어 사용한다.

조건부로 JSX를 포함하는 명령문을 이렇게 사용할 수 있다.

```react
let content; // content 선언
if (isLoggedIn) {
    content = <AdminPanel/>;
} else {content = <LoginForm/>}
}

return (
<div>
    {content}
        </div>)
```

`content`를 선언하고, JSX에서 변수를 사용하는 방식으로 조건부 렌더링하는 방식

더 간결한 식은 `조건 ? 응답` 형식을 사용하는 것이다.

```react
<div>
    {isLogedIn? 
        (<AdminPanel/>): (<LoginForm/>) }
</div>
```

더 짧게는 참일 때만 출력하는 컴포넌트를 `&&`를 사용해서 할 수 있다.

```react
<div>
    {isLogedIn && <AdminPanel/>}
</div>
```

```react
const products = [
    {title : 'Cabbage', id: 1},
        {title : 'Garlic', id: 2},
        {title : 'Apple', id: 3},
]
```

`map()`함수를 사용하면 컴포넌트 안에서 리스트 항목의 배열로 변환할 수 있다.

```react
const listItems = products.map(product => 
                              <li key={product.id}>{product.title}
                                  
                               </li>)
return (
<ul>{listItems}
        </ul>)
```

⚠리스트 아이템은 `key`속성을 가져야 한다. 리스트 안의 각 요소들은 형제 항목들 중에 자신을 고유하게 식별하는 문자열이나 숫자를 전달받아야 한다. 이 키는 나중에 항목을 삽입, 삭제 또는 재정렬하는 경우 등의 작업을 위해 가지고 있어야 한다.

```react
const products = [
      { title: 'Cabbage', isFruit: false, id: 1 },
  { title: 'Garlic', isFruit: false, id: 2 },
  { title: 'Apple', isFruit: true, id: 3 },
]; //products 는 야채 과일 객체를 가진 배열이다.

export default function ShoppingList() {
    const listItems = producs.map(product => <li                                   key={product.id}
                                      style={{color: product.isFruit? 'magenta' : 'darkgreen'}} {/* 스타일 속성은 리스트 아이템 각 하나의 isFruit 속성에 의존한다. */}>
                                      {product.title}

                                  </li>)
}
```



컴포넌트에서 이벤트 핸들러 함수를 선언하여 이벤트에 응답할 수 있다.

```react
function MyButton() {
    function handleClick() {
        alert("You Clicked Me!")
    }
    
    return (
    <button onClick={handleClick}>
            Click me
        </button>)
}
```

⚠ `onClick` 으로 전달받은 함수는 호출로써 전달하지 말 것. 그냥 전달만 할 것.



컴포넌트에 상태 추가하기

```react
import {useState} from 'react';
```

`useState`로 상태 변수를 선언할 수 있다.

```react
function MyButton () {
    const [count, setCount] = useStaet(0);
}
```

