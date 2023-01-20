# useContext

> props 드릴링 문제를 해결하기 위해 contextAPI를 활용



- Context 생성(작성 방법)

```react
const MyContext = React.createContext(defaultValue)
```



- Context Porvider를 통한 데이터 공급

  > context 안에 위치할 자식 컴포넌트 감싸기

```react
<MyContext.Provider value={전역으로 전달하고자하는 값}>
(자식 컴포넌트)
</MyContext.Provider>
```



defaultValue의 값으로 어떤 값을 넣을까?

- 일단은 안에 아무 값도 안 넣고 시작



- context도 컴포넌트처럼 내보내줘야 한다. default 없이 => 파일 하나당 하나만 사용할 수 있게 되기 때문에(여러 번 써야 하니까 default 없이)

  => ex 모듈 시스템에 대해 공부하면 이해할 수 있을 것

- `App()`의 최상위태그를 provider로 바꿔줌.

- `value={}` prop으로 전달한 값은 언제든지 자식 컴포넌트에서 사용할 수 있게 된다. 전달할 value 값은 개수 제한없이 전달 가능하다.





- 자식 컴포넌트에서 context 사용해보기

`DiaryList.js`

원래 `diaryList` prop을 받아서 사용하고 있었지만, 이제 context에서 꺼내와 사용할 수 있다.

=> Provider가 prop으로 전달한 context는  `useContext` hook으로 가져올 수 있다.

DiaryStateContext.Provider -> value -> const DiaryStateContext -> import DiaryStateContext -> useContext(DiaryStateContext)

```react
const diaryList = useContext
```



실제 props 드릴링은 함수 전달에서 발생했음.(`onRemove`, `onEdit` 등)

상태변화를 주도하는 함수들도 context를 통해서 전역에서 공급이 가능하다.

Provider도 컴포넌트이기 때문에 prop이 바뀌면 재생성된다. Provider 컴포넌트가 재생성되면 하위 컴포넌트들도 다 재생성 

​	prop이 변경된다는 것의 의미가 뭐지?

- data를 공급하는 provider와 함수를 공급하는 propvider를 *중첩하면* 된다.

```react
export const DiaryDispatchContext = React.createContext()
```

DiaryStateContext.Provider 바로 아래에 나머지 자식 요소 감싸서 배치

```react
<DiaryStateContext.Provider value={data}>
    <DiaryDispatchContext>
        <div className="App">
            <LifeCycle />
            <DiaryEditor onCreate={onCreate} />
            {/* App의 자식으로 배치 */}
            {/* dummyList - 배열 dummyList를 diaryList라는 이름으로 DiaryList의 prop으로 전달 */}
            {/* DiaryList의 컴포넌트에서 prop으로 전달받을 수 있음. */}
            <DiaryList onEdit={onEdit} onRemove={onRemove} />
        </div>
    </DiaryDispatchContext>
</DiaryStateContext.Provider>
```



- dispatch 함수 묶기(재렌더링 되지 않도록 useMemo 사용)

  ```react
  const memoizedDispatches = useMemo(() => {
      return { onCreate, onRemove, onEdit }
  }, []) // 리렌더링 되지 않도록 빈 배열 전달 
  ```

  