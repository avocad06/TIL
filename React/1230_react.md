`props` : 부모 컴포넌트에서 자식 컴포넌트에게 이름을 붙여서 값을 전달하는 방식

전달을 했으면 자식 컴포넌트에서 받아 써야 함.

```react
const Counter = (props) => {
    ...
}
```

=> *매개변수를* 활용하여 `객체` 형태로 받을 수 있음.

몇 개를 보내든 객체 안에 담을 수 있고, 이를 자식 컴포넌트에서 사용하는 방법은 점 표기법으로 값에 접근이 가능함. 



부모 컴포넌트에서 `initialValue`라는 이름으로 보낸 `props`를 매개변수를 이용해 객체 형태로 받아와서 점 표기법으로 값에 접근하여 자식 컴포넌트에서 사용할 수 있음.

```react
props.initialValue
```

```react
const [count, setCount] = useState(props.initialValue);
```



(전달해야하는 값이 많다면,)객체로 선언하고 부모 컴포넌트에서 객체 자체를 전달할 수도 있음.

```react
// 객체 선언
const counterProps = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
    e: 5,
}
```

```react
<Counter {...counterProps}/> //스프레드 연산자로 자식에게 전달
```

```react
// 비구조화 할당으로 객체를 전달할 수도 있음(countreProps객체 안의 initialValue 키의 값)
const Counter = ({initialValue}) => {
    const [count, setCount] = useState(initialValue);
    ...
}
```



특정 props가 `undefined`로 전달될 수도 있는 상황이라면

`defaultPops`를 설정하여 에러를 미연에 방지

```react
Counter.defaultProps = {
    initialVlue : 0,
}
```



자식 컴포넌트에게 동적인 데이터를 전달하려면?

`OddEvenResult` 컴포넌트에 `Counter` 컴포넌트의 `count` state를 전달하려면?

=> `OddEvenResult` 컴포넌트를 `Counter`의 자식요소로 배치



리액트의 컴포넌트는 부모가 내려주는 props가 변경이 되면, 자식 컴포넌트도 rerender

props를 받지 않아도 자식 컴포넌트도 rerender된다.



리액트의 컴포넌트는 가지고 있는 state가 바뀔때마다 리랜더

내려온 props가 변경될 때마다 리랜더

그게 아니어도 부모 컴포넌트가 리랜더 될 때마다 자식 컴포넌트도 리랜더

* 리랜더가 된다는 것 : 컴포넌트 함수가 다시 호출된다는 것



컴포넌트 자체도 props로 전달할 수 있다.

*컴포넌트를 컴포넌트로 감쌀 수 있다.*

props는 부모 컴포넌트가 자식 컴포넌트에게 값을 전달해주는 건데.

그러면 `이 상황`에서 부모 컴포넌트는 누구지?

지금 부모 컴포넌트는 `Container`고,

부모 컴포넌트가 보내주고 있는 컴포넌트 children props를 다시 `Container`가 받고 있는데,

props는 부모와 자식 컴포넌트에서만 성립하는 게 아닌가?

근데 그러면 지금 최상위 태그가 없는 상태인데(`Container` 컴포넌트가 가장 바깥이니까)



