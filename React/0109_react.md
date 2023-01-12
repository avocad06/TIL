전역적으로 공급되는 prop의 이름을 바꾸면 다른 공급받는 prop들의 이름도 바꿔줘야 해서 불편하다. => 나중에 해결방법에 대해 배움.(contextAPI)



- div내에서 삼항연산자 말고 if문을 이용해서 출력할 컴포넌트를 결정할 수는 없을까?



수정 기능

아이템 각각이 수정 버튼을 가져야 한다.

수정하기를 누르면 본문 내용이 아니라 입력 form이 나올 수 있도록 한다.

`isEdit` state의 초기값은 false로 한다.

```react
const toggleIsEdit = () => setIsEdit(!isEdit);
```

`toggleIsEdit`은 호출 될 때 `setIsEdit` 상태변화 함수를 호출하여 현재 `isEdit`state의 **반전 상태**로 바꿔주는 역할을 하는 함수이다.



`isEdit` state가 true일 때는 컨텐츠가 아닌 폼을 보여주고, false일 때는 컨텐츠를 보여준다.

> 삼항 연산자 활용 : true라면 form, false라면 contents

```react
{isEdit ? <></>:<></>}
```



textarea에 입력되는 값(input)을 핸들링하기 위한 state

```react
const [localContent, setLocalContent] = useSteate("");
```



`onChange`가 호출될 때마다 `setLocalContent`함수가 호출되어 `localContent` state를 변화시킴

```javascript
console.log(localContent)
```

```
21세기의 어떤 ㄴ
DiaryItem.js:8 21세기의 어떤 나
DiaryItem.js:8 21세기의 어떤 나
DiaryItem.js:8 21세기의 어떤 날
DiaryItem.js:8 21세기의 어떤 날
DiaryItem.js:8 21세기의 어떤 나
```

state에 data처럼 <u>완성된 형태가 저장되는 것만은 아니다.</u>(data는 데이터가 조회되는 공간의 내용을 저장하고 있으므로 완성된 형태)

state는 단순히 상태변화 함수가 호출됨에 따라 인자로 받은 값으로 변화되는 값



textarea에 입력되는 값들도 리액트에서 핸들링하도록 만들어준다.

textarea의 input을 핸들링할 state



삭제하기의 onClick 함수가 기니까 전역으로 빼준다. `handleRemove`

=> handleRemove 함수는 DiaryItem의 삭제하기 버튼을 눌렀을 때 (onClick시 호출) <br>삭제할 건지 물어보고(window.confirm) 확인 시, `App.js`의 onRemove함수를 호출하며<br>삭제할 DiaryItem의 id 값을 매개변수로 전달하는 역할을 한다.(**state 끌어올리기, 이벤트 발생의 방향은 역방향**)



수정하기를 누르면 표시되는 버튼들도 달라져야 한다.

> 삼항 연산자를 이용 `isEdit` state에 따라

```react
isEdit ? 
    <button>수정 취소<button/>
    <button>수정 완료</button>
    :
    <button>수정하기<button/>
    <button>삭제하기</button>
```



수정 취소를 누르면 `isEdit` state를 false로 바꾸고 그에 따른 화면을 보여준다.

```react
<button onClick={toggleIsEdit}>수정 취소</button>
```



수정폼에 원본 데이터를 넣기

=> 수정 폼을 관리할 state(`localContent`)의 기본값을 content로 해주면됨.

하지만, 이렇게 하면 localContent의 내용이 수정하기 버튼을 마지막으로 눌렀을 때의 상태로 유지되게 된다.

```
ex) 원본 내용 : 만두

수정하기 눌러서 작성한 내용 : 김치만두 -> 수정취소로 취소

수정취소

다시 수정하기 누르면 나오는 내용: '원본 내용' 만두가 아니라 마지막으로 수정했던(하다 말았던) 김치만두
```

=> 수정 취소 버튼을 눌렀을 때 localContent의 내용을 다시 원본 content로 바꿔주면 됨.



- 함수를 새로 생성해서 onClick에 부여하나?

  => yes. `handleQuitEdit`

  ```react
   const handleQuitEdit = () => {
          setIsEdit(false);
          setLocalContent(content);
      }
  ```

  ```react
  <button onClick={handleQuitEdit}>수정 취소</button>
  ```

  

- 수정완료를 누르면, handleEdit 함수를 하나 만들어서 거기서 App.js의 onEdit 함수를 호출해서 id값과 content내용을 전달하나?

  => yes. `handleEdit` 함수는 useRef로 유효성 검사(내용이 5글자 이상인지)를 하고, 통과 후 수정하는 게 맞는지 확인하는 prompt 창에 확인을 눌렀을 때 App.js(부모 컴포넌트)로 targetId(id)와 newContent(localContent)를 전달하는 역할을 하는 함수
  
  ```react
  const handleEdit = () => {
      // 유효성 검사    
      if (localContent.length < 5) {
              localContentInput.current.focus();
              return;
          }
      // 수정확인 프롬프트
          if (window.confirm(`${id}번째 일기를 수정하시겠습니까?`)) {
              // 부모 컴포넌트로 targetId, newContent 전달
              onEdit(id, localContent);
              // 편집모드 종료
              // setIsEdit(!isEdit);
              toggleIsEdit(); // 같은 의미의 코드(편집 모드 종료)인데, 함수 호출이 더 성능상 좋을까? 아니면 state변화함수를 바로 호출하는 것이 성능상 좋을까?
          }
      }
  ```
  
  



# 자주 등장하는 오류(부모 엘리먼트)

```
SyntaxError: D:\react-practice\simple-diary\src\DiaryItem.js: Adjacent JSX elements must be wrapped in an enclosing tag. Did you want a JSX fragment <>...</>? (33:12)
```

- 감싸고 있는 div가 분명히 있는데 왜 enclosing tag를 자꾸 요구할까?
- JSX elements의 범위가 어디야?
- 그냥 div일 땐 아무 오류가 안 났는데 조건문으로 랜더링하니까 (감싸지 않으면)저런 오류가 생긴다.

- 이전에 diartyLst도 그랬는데, 무슨 기준인지??



# async, await

오랜 작업이 걸리는 일은 

Promise((resolve, reject) => {

})

프로미스 팬딩 상태 : resolve/reject 아무것도 호출하지 않은 상태

프로미스를 이용하지 않아도 자동으로 함수안의 항목들이 프로미스로 바뀌는 키워드 async

프로미스를 더 간편하게 쓸 수 있는 방법



await

async가 붙은 함수 안에서만 사용 가능

chaining을 하는 것보다 동기적으로 실행되는 것처럼 보이게 하는 키워드



