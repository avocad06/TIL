js의 state가 갖는 값은 휘발성 메모리다.

데이터베이스에 값을 저장하고 데이터베이스에서 값을 가져오게 만들어야 한다.



# Web Storage API

> 브라우저에서 키/값 쌍(JSON)을 쿠키보다 훨씬 직관적으로 저장

- session storage

  

- local stroage

  > 브라우저를 닫았다 열어도 데이터가 남아있음.(껐다 켜도 유지됨)



local Storage라는 데이터베이스에서 값을 사용하는 방식



## local Storage에 값 저장하기

```react
useEffect( () => {
    localStorage.setItem('key', 10)
}, [])
```

local Storage에 {'key' : 10} 키 값 쌍을 저장하라는 의미

브라우저의 개발자도구 - 어플리케이션 - 로컬 스토리지 탭에서 로컬스토리지를 확인할 수 있음.

로컬스토리지에 value값으로 객체를 저장하려면 `JSON.stringify()` 메서드로 ***직렬화*** 시켜줘야 한다.

- 직렬화? 객체를 문자열 형으로 바꿔준다.



로컬스토리지에 한번 저장된 값은 저장 코드가 지워져도 브라우저의 스토리지를 비우지 않는 한 유지된다.



로컬 스토리지의 값을 꺼내오는 방법

```react
const item1 = localStorage.getItem('item1');
```



로컬스토리지에 들어가는 값들은 다 문자열로 변환된다.

객체도 문자열로 변환되어 반환된다.

=> 직렬화된 객체를 `JSON.parse()` 메서드로 다시 js 객체로 복원시켜줘야 한다.



일기 데이터를 로컬스토리지에 저장하려면?

state를 그대로 setItem() 에 전달하면 되나?

- 일기 데이터를 변경할 때마다 로컬 스토리지에 값을 추가한다.
- `data` state를 관리하고 있는 함수 reducer에 로컬 스토리지에 값을 저장하는 로직을 추가한다. `data` state는 배열이기 때문에 `JSON.stringify()`로 직렬화시켜줘야 한다.



##  오류 발생

- reducer로 `CREATE`를 실행했는데도 새로운 데이터가 추가되는 게 아니라 기존 데이터가 수정되는 현상이 발생함.

- 콘솔 오류메시지

  > 배열 각 요소의 key가 없다.

  ```javascript
  Warning: Each child in a list should have a unique "key" prop. Check the render method of `DiaryEditor`.
  ```



`DiaryEditor.js`

```react
{emotionList.map((it) => <EmotionItem key={it.emotin_id} />)}
```

`it.emotin_id`로 오타가 나서 emotionList 배열 안 객체 요소의 `emotion_id` 프로퍼티를 참조하지 못했기 때문에 정의된 값이 없고, key가 설정되지 않은 현상이다.

오타를 `emotion_id`로 고쳐주면 데이터가 로컬 스토리지에 문제없이 저장되는 것을 확인할 수 있다.



- 일기 에디터에 삭제 버튼 기능 구현

  `MyButton` 컴포넌트에 rightchild로 삭제하기 버튼 만들기

  누르면 onClick했을 때 onRemove함수에 삭제하고자 하는 일기의 id 값을 전달하도록 함수 호출하는 `handleRemove` 함수 생성해서 `MyButton`컴포넌트의 `onClick` prop으로 전달하기

  => 삭제하기 버튼은 일기 에디터가 수정 상태일 때만 볼 수 있게 한다.

  수정 상태인지 아닌지에 따라서 아무것도 없게 하거나 삭제하기 버튼을 띄운다.(수정 상태가 참일 때만 삭제하기 버튼을 띄운다 -> 단락회로 평가 이용)

  ```react
  {is Edit && <MyButton text={"삭제하기"} type={"negative"}/>}
  ```

  삭제하기 버튼을 눌렀을 때 이벤트 핸들러 함수 `handleRemove`

- `onRemove` 함수는 어디서 가져올 수 있나? 우리가 provider로 공급하고 있는 DiaryDispatchContext를 useContext()로 호출해서 가져올 수 있다.



- 컴포넌트가 마운트될 때 로컬 스토리지에서 값 꺼내오기(`getItem`)

  내가 생각한 방식:

  useEffect(() => {localStorage.getItem('diary')}, []) 이지 않을까? 근데 value 값이 배열의 형태니까 JASON.parse() 써줘야할 거 같다.

  그걸 현재 data state에다 넣어주면 될 거 같다.

  => id 값에 대한 처리가 필요하다. 

  

  만약 내가 생각한 방식대로만 하면,

  ```react
  useEffect(() => {
      dispatch({ type: "INIT", data: JSON.parse(localStorage.getItem("diary")) })
    }, [])
  ```

  ```javascript
  Warning: Encountered two children with the same key, `0`.
  ```

  `Encountered` 오류메시지가 출력된다. => id값에 대한 처리를 해 주지 않았기 때문에

   

  발생원인

  ```react
  const dataId = useRef(0);
  ```

  id 값이 0부터 시작하기 때문이다.

  

  왜 중복돼서 값이 들어가는가?

  ```react
   const onCreate = (date, content, emotion) => {
      dispatch(
        {
          type: "CREATE",
          data: {
            id: dataId.current,},
      dataId.current += 1;
    };
  ```

  onCreate 함수가 dataId.current를 참조하고 있기 때문이다. dataId의 초기값은 0이기 때문에, 새로고침되면 dataId는 계속 0으로 초기화된다.

  컴포넌트 마운트 시에 데이터베이스(localStorage 포함)에서 가져와서 값을 출력하게 되면 이전 id 값이 저장되어 있기 때문에 새로고침 후 작성한 다이어리들은 초기화된 0값부터 다시 시작하여 데이터베이스에 기존에 존재하는 데이터들의 id 값과 중복되는 값을 가지게 된다.

  따라서, id 값을 처리해서 데이터베이스에 저장되어있는 가장 최신의 id 값 다음부터 id 값을 시작해야 중복을 피할 수 있다.



- id 값 처리

  데이터베이스(localStorage)에 있는 id 값들을 기준으로 내림차순으로 정렬해서 가장 최신에 있는 데이터의 id 값을 가져와서  `dataId.current`를 최신 id 값 + 1로 처리해주면 된다.

  ```react
  if (localData) {
      const diaryList = JSON.parse(localData).sort(
      (a, b) => parseInt(b.id) - parseInt(a.id))
      dataId.current = parseInt(diaryList[0].id) + 1
      
      dispatch({type: "INIT", data: diaryList})
  }
  ```

  