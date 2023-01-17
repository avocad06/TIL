App 컴포넌트에는 상태변화 처리 함수가 존재

상태를 업데이트하기 위해서는 기존의 상태를 참조해야했기 때문에 컴포넌트 내에 존재해야했고, 이렇게 함수가 늘어나고 길어지는 건 좋은 방식이 아님. => 그럼 어떻게? *컴포넌트 밖으로 분리하자*



# useReducer

> 컴포넌트에서 상태변화 로직을 분리하자
>
> useState처럼 상태 관리를 돕는 react hooks
>
> 컴포넌트를 더 가볍게

- 이전 코드

  `<App.js>`

  - 함수를 `App.js`내에서 정의하고<br>(`onCreate`, `onRemove`, `onEdit`)

    ```react
      const onCreate = (author, content, emotion) => {
        const created_at = new Date().getTime();
        const newItem = {
          author,
          content,
          emotion,
          created_at,
          id: dataId.current
        }
        dataId.current += 1;
        setData([newItem, ...data]);
      };
    
      const onRemove = (targetId) => {
        console.log(`${targetId}가 삭제되었습니다.`);
        const newDiaryList = data.filter((it) => it.id !== targetId);
        setData(newDiaryList);
      };
    
      const onEdit = (targetId, newContent) => {
        setData(
          data.map((it) =>
            it.id === targetId ?
              { ...it, content: newContent } : it
          ))
    
      }
    ```

  - 하나씩 props로 내려줘야 했음.

    ```react
    <DiaryEditor onCreate={onCreate} />
          <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} DummyList={dummyList} />
    ```

  하지만, 이런 상태 변화 로직이 많아진다면?

  useReducer를 활용하면 reducer라는 함수를 컴포넌트 밖으로 분리하여 다양한 상태변화 로직을 switch/case문처럼 처리할 수 있도록 함.

  ```react
  const [상태, dispatch] = useReducer(reducer, 초기값)
  ```

  - `상태`는 관리할 state
  - `dispatch`는 상태를 변화시키는 action을 발생(raise)시키는 함수
  - `reducer`는 dispatch로 발생한 상태 변화를 처리해주는 함수
  - 초기값은 `상태` state의 초기값

  => ex) 초기값이 1인 count state에 dispatch 함수를 호출해서 상태 변화가 일어나면 reducer 함수가 상태 변화를 처리한다.

dispatch는 호출될 때 매개변수로 action객체를 전달하게 된다.

- action = 상태변화 를 의미 

이 action객체는 reducer로 날아가게 됨. reducer함수는  dispatch가 호출되면 호출됨.(상태변화가 일어났을 때 호출된다는 의미)

reducer는 첫번째 인자로는 현재 state, 두 번째 인자로는 전달받은 action객체를 가짐.

- state : 상태변화가 일어나기 직전의 state
- action : 어떤 상태 변화를 일으켜야 하는지 정보가 담겨 있음.

```react
const reducer = (state, action) => {}
```

dispatch는 reducer함수를 호출하고, action객체를 전달하는 역할

- 어떻게 전달받은 state인 걸 알 수 있지?
- reducer는 한 번밖에 쓰이지 않는 건가 ?
- 아니면 reducer를 정의할 때 state에다가 관리할 state를 맵핑시키는건가 ?
- 상태변화를 처리하는 `reducer`함수는 직접 선언해 줘야 함.

useReducer를 사용하는 이유는 복잡한 상태관리 로직을 컴포넌트 밖에서 관리하기 위함. 따라서 `reducer`함수를 `App`밖에서 선언함.



```
dispatch를 호출하면 reducer가 실행되고, reducer가 return하는 값이 data의 값이 된다.
```



어떤 type의 액션이 존재할 수 있는지 확인

(API 호출)getData : 한 방에 데이터를 초기화한다.(`INIT`)

```ㄱㄷㅁㅊㅅ
setData(initData)
```



onCreate : 데이터를 전체 데이터에 추가한다(`CREATE`)

```react
setData((data) => [newItem, ... data])
```



onRemove : 전달받은 id값을 가진 데이터를 제외한 데이터들만 필터링한다(`REMOVE`)

```react
setData((data) => data.filter(data.id != targetId))
```



onEdit : 전달받은 id 값이 일치하면 해당 데이터의 content값만 전달받은 수정값으로 갱신한다(`EDIT`)

```react
setData(data.map((it) => it.id === targetId?
                {...it, content: newContent} : it))
```



reducer함수는 상태변화를 처리하는 함수이기 때문에 일어난 새로운 state를 반환해야 한다. 위에서 정의한 액션들과 일치하는 상태변화가 일어나지 않았을 경우(ex) type이 잘못전달, 오타 등) 원래의 state를 그대로 반환한다.

```react
default :
	return state
```



`getData`

```react
dispatch({type:"INIT", data:initData})
```

action 객체 안에는 type, data 프로퍼티가 들어가게 됨.

action객체는 어떤 상태 변화를 일으켜야 하는지의 정보가 담겨 있으므로, (마운트 시)초기화 할 데이터를 action 객체 안에 담아서 전달한다.

이로써 reducer 함수는 

1. 어떤 상태 변화가 일어났는지 알 수 있고 : `INIT`
2. initData를 반환할 수있게 됨. :  `return action.data`

=>  `data` state의 새로운 state가 반환됨.



`onCreate`

```react
    dispatch({ type: 'CREATE', data: { author, content, emotion, id: dataId.current } })
```

```react
const reducer = (state, action) => {
    case 'CREATE': {
      const created_date = new Date().getTime();
      const newItem = {
        ...action.data,
        created_date,
      }
      return [newItem, ...state]
    }   
  }
```



- 객체의 비구조화 할당에서 이런 것도 가능한 문법인가?

  ```react
  data: { 
      author, 
      content, 
      emotion, 
      id: dataId.current } 
  ```

  id 프로퍼티만 키와 value가 명시되어 있음

  => ㄴㄴ <u>비구조화 할당이 아니라 *단축 프로퍼티 문법*</u>임!

  author와 content, emotion이라는 키 이름이랑 변수의 이름이 같음

  변수를 사용해 프로퍼티를 만드는 경우 값과 변수의 이름이 동일하면 변수의 이름을 키로, 변수의 값을 value로 가진 프로퍼티를 생성할 수 있음.

  일반 프로퍼티와 단축 프로퍼티를 함께 사용하는 것도 가능함.

  ```javascript
  let user = {
      name,
      age : 30,
  }
  ```

- 이런 것도 가능하긴 하더라구

  위에서 data라는 키 안에 새로운 객체를 생성해서 reducer한테 보내줬는데, dispatch 호출 전 기존에 있었던 `newItem`을 나머지 연산자로 data 키에 담아서 보내줄 수도 있음.

  => but, 우리가 reducer로 상태 로직을 관리하는 이유는 <u>길어지는 `App()`을 최적화하기 위해서</u>임. 따라서, App내에서 선언하기 보다 컴포넌트 밖에 있는 reducer함수에게 값을 보내서 그 내에서 선언하게 하는 것이 좋다! 내 생각엔 그럽니다....(아래는 정상 작동)

  ```react
  const onCreate = (author, content, emotion) => {
  
      const created_at = new Date().getTime();
      const newItem = {
        author,
        content,
        emotion,
        created_at,
        id: dataId.current
      }
      dispatch({ type: 'CREATE', data: { ...newItem } })
      dataId.current += 1;
    };
  ```

  ```react
  const reducer = (state, action) => {
    switch (action.type) {
        case 'CREATE':
            return [{ ...action.data }, ...state] 
    }
  ```

  

`onRemove`

- onRemove 함수는 전달받은 targetId값을 가진 데이터를 제외한 data를 필터링해서 새로운 state를 반환하는 함수

- type : 'REMOVE', id를 전달해서 case문 안에서 filter 하려나?

  => 정답. data전체를 전달할 필요없이 id값만 전달하면 됨.

```react
    dispatch({ type: 'REMOVE', targetId })
```

```react
const reducer = (state, action) => {
  switch (action.type) {
      case 'REMOVE': {
          return state.filter((it) => it.id !== action.targetId)
    }          
  }
```



`onEdit`

- onEdit 함수도 똑같이 원래 함수 안에서 했던 선언들을 case문 안에서 한다고 보면 될 거 같음.

- onEdit은 targetId와 같은 값을 가진 데이터의 content를 바꾸는 함수이므로 onCreate했던 것처럼 data 객체의 형식으로 보내지 않을까?

  => 객체 형식 말고 그냥 변수로 보내긴 했음.

```react
    dispatch({ type: 'EDIT', targetId, newContent })
```

```react
const reducer = (state, action) => {
    switch (action.type) {
        case 'EDIT': {
            return state.map((it) => action.targetId === it.id ?
        { ...it, content: action.newContent } : it)
    }
}
```



- 이게 해 보니까 useRducer를 사용하면 이전에는 setState내에서 했던 작업을 switch - case문 안에서 하면 된다 라는 기본 컨셉
- setData를 여러 번 안 써도 되고, useState로 관리하지 않아도 됨.
- 여러 로직이 있으니까 가능한 것(init, create, remove, edit)



