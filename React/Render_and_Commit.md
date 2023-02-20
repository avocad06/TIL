# Render_and_Commit

> 리액트에서 의미하는 '렌더링'
>
> 렌더링은 언제, 왜 일어나는가
>
> 컴포넌트를 화면에 표시하는 단계
>
> 렌더링이 항상 DOM을 업데이트시키지는 않는 이유

렌더링을 레스토랑에 비유해 보면, 

1. 손님의 주문을 주방으로 전달하는 것은 

   렌더링을 유발시키는 것이다.

2. 주문에 따라 주방에서 조리를 하는 것은 

   컴포넌트를 렌더링하는 것이고, 

3. 테이블로 서빙하는 것은 

   DOM에 커밋하는 것이다. 



## Trigger a render

컴포넌트를 렌더링하는 이유 2가지

1. 컴포넌트의 **initial render**(초기 렌더링)
2. 컴포넌트 자신이나 부모 컴포넌트의 state가 업데이트되었을 때



### Initial Render

> 초기 렌더링

앱이 시작되면 초기 렌더링이 일어나야 한다. 초기 렌더링은 `createRoot`와 그 대상이 되는 DOM 노드(`<img />`)를 호출하여 render메서드를 컴포넌트에 호출함으로써 수행된다.

```javascript
import { createRoot } from 'react-dom/client';
```

```javascript
const root = createRoot(document.getElementById('root'))
root.render(<Image />);
```



### Re-renders when state updates

> state 업데이트로 인한 리렌더링

컴포넌트가 초기에 한 번 렌더되고 나면, `'set-*` 상태 변화 함수로 state를 업데이트 시키면서 추가 렌더링을 시킬 수 있다.



## React renders your components

> 리액트가 컴포넌트를 렌더링한다는 것

리액트는 렌더링을 하게 되면 화면에 어떤 것을 보여줄지 파악하기 위해 컴포넌트를 호출한다.

렌더링이란 리액트가 컴포넌트를 호출하는 것이다.

- 초기 렌더링에서 리액트는 root 컴포넌트를 호출한다.
- 이후의 렌더링에서는 리액트가 state 업데이트로 렌더링을 트리거한 함수형 컴포넌트를 호출한다.

리액트는 이전 렌더링 이후에 변경된 속성이 있는 경우 이를 계산한다. 다음 단계인 커밋 단계 전에는 <u>해당 정보로 아무 작업도 수행하지 않는다.</u>



## React commits changes to the DOM!

> 변경사항을 DOM에 커밋한다.

리액트는 렌더링 간 *차이가 있는 경우*에만 DOM 노드를 변경한다.

