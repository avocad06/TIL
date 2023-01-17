App 컴포넌트에는 상태변화 처리 함수가 존재

상태를 업데이트하기 위해서는 기존의 상태를 참조해야했기 때문에 컴포넌트 내에 존재해야했고, 이렇게 함수가 늘어나고 길어지는 건 좋은 방식이 아님. => 그럼 어떻게? 컴포넌트 밖으로 분리하자



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

useReducer를 사용하는 이유는 복잡한 상태관리 로직을 컴포넌트 밖에서 관리하기 위함.



```
dispatch를 호출하면 reducer가 실행되고, reducer가 return하는 값이 data의 값이 된다.
```

