상태에 어떠한 변화가 필요하게 될 때 액션이 발생한다.

```
무엇이 일어났는지 설명
```



액션은 하나의 객체로 표현되는데, 액션 객체는 다음과 같이 `type`을 프로퍼티로 가지는 객체가 된다.

```react
{
    type: "TOGGLE_VALUE"
}
```

액션 객체에는 `type`외의 값들을 추가할 수 있지만, `type`은 필수적으로 가지고 있어야 한다.

```react
{
    type: "ADD_TODO",
    data: {
        id: 0,
            text: "리덕스 배우기"
    }
}
```

```react
{
    type: "CHANGE_INPUT",
    text: "안녕하세요"
}
```



액션 생성함수 (Action Creator)

> 액션 생성함수는 액션을 만드는 함수이다. 단순히 파라미터를 받아와서 액션 객체 형태로 만들어준다.

```react
export function addTodo(data) {
    return {
        type: "ADD_TODO",
        data
    };
}

// 화살표 함수로도 가능하다.
export const changeInput = text  => ({
    type: "CHANGE_INPUT",
    text
})
```

이러한 액션 생성함수를 만들어서 사용하는 이유는 나중에 컴포넌트에서 더욱 쉽게 액션을 발생시키기 위함이다. 보통 함수 앞에 `export` 키워드를 붙여서 다른 파일에서 불러와서 사용한다.



리듀서(Reducer)

> 리듀서는 변화를 일으키는 함수이다. 리듀서는 두 가지의 파라미터를 받는다.

```
이전 state와 action 객체를 받은 후에 변화된 state를 return하는 것
```



```react
function reducer(state, action) {
    // 상태 업데이트 로직
    return alteredState;
}
```



리듀서는, 현재의 상태와, 전달 받은 액션을 참고하여 새로운 상태를 만들어 반환한다. 리듀서는 `useReducer`를 사용할 때 작성하는 리듀서와 똑같은 형태를 가지고 있다. 

예를 들어, 카운터를 위한 리듀서를 작성한다면 다음과 같다.

```react
function counter(state, action) {
    switch (action.type) {
        case 'INCREASE':
            return state + 1;
        case 'DECREASE':
            return state - 1;
        default:
            return state;
    }
}
```

`useReducer`에서는 일반적으로 `default` 부분에 `throw new Error('Unhandled Action')`과 같이 에러를 발생시키도록 처리하는 게 일반적인 반면 리덕스의 리듀서에서는 기존 `state`를 그대로 반환하도록 작성해야 한다.

리덕스를 사용할 때에는 여러 개의 리듀서를 만들고 이를 합쳐서 루트 리듀서를 만들 수 있다. (루트 리듀서 안에 작은 리듀서들을 서브 리듀서라고 부른다.)



스토어(Store)

> 리덕에스에서는 한 애플리케이션당 하나의 스토어를 만들게 된다. 스토어 안에는, 현재의 앱 상태와, 리듀서가 들어가 있고, 몇 가지 내장 함수가 들어가 있다.

```
state를 감싸주는 역할을 한다. store 안에 존재하는 메서드들을 이용하여 state 관리가 가능하다.
```



- 디스패치(dispatch)

  > 스토어의 내장함수 중 하나, 액션을 발생시키는 것.

  dispatch 함수에는 액션을 파라미터로 전달한다. `dispatch(action)` 

  dispatch를 호출하면 스토어는 리듀서 함수를 실행시켜서 해당 액션을 처리하는 로직이 있다면 액션을 참고하여 새로운 상태를 만들어 준다.

- 구독(subscribe)

  > 스토어의 내장함수 중 하나, 함수 형태의 값을 파라미터로 받음.

  subscribe함수에 특정 함수를 전달하게 되면, 액션이 디스패치되었을 때마다 전달해준 함수가 호출된다. 리덕스에서 자주 쓰지는 않고, 대신에 react-redux 라이브러리에서 제공하는 `connect` 함수 또는 `useSelector` 훅을 사용하여 리덕스 스토어의 상태에 구독한다.



액션의 타입 => state를 변화시킬 상태를 정의

액션 생성함수 => 어떤 액션이 일어났는지 리듀서에 전달

리듀서는 발생한 변화의 정보를 액션 객체로 전달받고, 처리.



리덕스 모듈이란 액션타입, 액션 생성함수 ,리듀서가 모두 들어있는 자바스크립트 파일을 의미한다.



- redux-promise, redux-thunk

  > redux를 더 잘 쓸 수 있게 도와주는 미들웨어라고 이해하면 된다.

  - redux 에는 store가 있고, store 안에서 모든 state을 관리. store 안에 있는 state을 변경하려면 dispatch > action 을 통해 할 수 있음. action은 객체의 형식이어야 함. 그래야 store가 받을 수 있음. store에서 promise형식으로 받을 때도 있고, function 형태로 된 것을 받을 때도 있음.
  - redux-thunk 는 dispatch한테 어떻게 function을 받는지 알려줌
  - redux-promise같은 경우는 어떻게 promise가 왔을 때 대처해야하는지 알려주는 역할을 함



# Redux 사용하기

`index.js`

provider를 import 해서 app컴포넌트를 감싸준다.(redux와 어플리케이션을 연결)

```react
    <Provider>
      <App />
    </Provider>
```

미들웨어를 이용해야 redux store가 promise도 받을 수 있다.

applyMiddleWare import 후 추가

```react
const createStoreWithMiddleware = applyMiddleware()
```



combineReducer => 다양한 reducer들이 있을 수 있음. reducer 안에서는 state가 어떻게 변화하는지 보여주고, 변화한 값을 return하기 때문에(여러 state이 있을 수 있기 때문에) combineReducers는 rootReducer에서 <u>합쳐주는 역할을 함!</u>

```react
const rootReducer = combineReducer({
    user,
    comment,
})
```



Dispatch를 이용해서 Action을 취하고 Reducer로 가는 방향

