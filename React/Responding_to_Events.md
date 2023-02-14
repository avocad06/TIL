# Responding to Events

> 이벤트 핸들러를 작성하는 다양한 방법
>
> 부모 구성요소로부터 이벤트 처리 핸들링을 전달하는 법
>
> 이벤트 전파 및 중지 방법

유저가 클릭했을 때 메시지를 alert시키려면

1. `Button` 컴포넌트 안에 `handleClick`함수를 선언한다.

2. `handleClick`함수는 메시지를 alert하는 함수이다.

3. `<button>` JSX에 `onClick={handleClick}` 을 추가한다.

   => `handleClick`함수를 선언해서 `<buton>` 에 prop으로 전달한 것.

   *prop : 소품

*이벤트 핸들러(`handleClick`)* 

- 이벤트핸들러는 보통 컴포넌트 안에 정의된다.

- `handle`로 시작하고 그 뒤에 이벤트 이름이 온다.

  ex) `onMouseEnter={handleMouseEnter}`

JSX에서 인라인으로 이벤트핸들러를 정의할 수도 있다.

```react
<button onClick={function handlerClick() {
        alert('You clicked me!')
    }}>
</button>
```

화살표함수도 가능!

```react
<button onClick={() => {alert('You clicked me!')}}></button>
```



이벤트 핸들러에 전달되는 함수는 호출되는 것이 아니라 전달되어야 한다.

- 함수 전달 : 사용자가 버튼을 클릭할 때만 함수를 호출하도록 지시
- 함수 호출(wrong) : 렌더링 중에 즉시 함수를 실행(렌더될 때마다 실행)



컴포넌트로 감싼다? => props.children[합성과props.children](https://developer-talk.tistory.com/226)- 태그와 태그 사이

`Toolbar` -> `PlayButton` `UploadButton` -> `Button + eventHandler`

```
Toolbar 컴포넌트 아래 PlayButton과 UploadButton 컴포넌트가 있고 각 버튼 컴포넌트들은 각기 다른 이벤트 핸들러를 prop으로 전달받는 Button 컴포넌트를 자식 컴포넌트로 가지고 있다.
```



예를들어, 버튼 컴포넌트의 온클릭 prop이 onSmash라는 이름으로 전달됐을 수 있다. 지금 함수 이름이 onSmash라는 거지

그치만 해당 함수의 이름이 onSmash라는 거고, button 태그에서 일어나는 onClick시 실행시킬 onSmash 함수라는 뜻이니까 상관이 없다.

규칙에 따라, 이벤트 핸들러 prop은 `on`으로 시작하고, 대문자가 뒤에 와야한다. 

규칙만 지키면 이름은 꼭 이벤트 이름이 아니라 앱별 개념에 대한 이름이어도 상관이 없다.

앱별 상호작용 후에 prop이름을 지정하면 재사용성이 증가한다.(유연성 증가)

`Toolbar`는 `onPlayMovie`가 뭐하는 함수인지 알 필요가 없다.(전달만 할 뿐이다)

키보드 단축키로 실행시킬 수도 있고, onClick으로 실행시킬수도 있기 때문에 이벤트 핸들러 prop의 이름은 앱별 상호작용 관련으로 하는 것이 좋다.

는 의미같음!

- 이벤트 전파

  onScroll 을 제외한 모든 이벤트는 전파된다.



*Stopping propagation*

```react
function Button({onClick, children}) {
  return (
    <button onClick={e => {
      e.stopPropagation();
      onClick();
    }}>
      {children}
    </button>
  )
}
```

1. 리액트는 `<button>`에 전달된 `onClick`핸들러를 호출한다.
2. onClick 핸들러는 버블링을 막고, `Toolbar` 컴포넌트로부터 prop으로 전달받은 onClick 함수를 호출한다.
3. `Toolbar`컴포넌트에 정의된 이 함수는 버튼이 자신만의 alert를 할 수 있도록 보여준다.
4. 이벤트 전파가 중지되었기 때문에 부모요소의 `onClick`핸들러는 동작하지 않는다.

