전역적으로 공급되는 prop의 이름을 바꾸면 다른 공급받는 prop들의 이름도 바꿔줘야 해서 불편하다. => 나중에 해결방법에 대해 배움.



수정 기능

아이템 각각이 수정 버튼을 가져야 한다.

수정하기를 누르면 본문 내용이 아니라 입력 form이 나올 수 있도록 한다.

`isEdit` state의 초기값은 false로 한다.

```react
const toggleIsEdit = () => setIsEdit(!isEdit);
```

`toggleIsEdit`은 호출 될 때 `setIsEdit` 상태변화 함수를 호출하여 현재 `isEdit`state의 반전 상태로 바꿔주는 역할을 하는 함수이다.



`isEdit` state가 true일 때는 컨텐츠가 아닌 폼을 보여주고, false일 때는 컨텐츠를 보여준다.

> 삼항 연산자 활용 : true라면 form, false라면 contents

```react
{isEdit ? <></>:<></>}
```



textarea에 입력되는 값(input)을 핸들링하기 위한 state

```react
const [localContent, setLocalContent] = useSteate("");
```

```react
console.log(localContent)
```

`onChange`가 호출될 때마다 `setLocalContent`함수가 호출되어 `localContent` state를 변화시킴

```
21세기의 어떤 ㄴ
DiaryItem.js:8 21세기의 어떤 나
DiaryItem.js:8 21세기의 어떤 나
DiaryItem.js:8 21세기의 어떤 날
DiaryItem.js:8 21세기의 어떤 날
DiaryItem.js:8 21세기의 어떤 나
```

state에 data처럼 완성된 형태가 저장되는 것만은 아니다.

state는 단순히 상태변화 함수가 호출됨에 따라 인자로 받은 값으로 변화되는 값



textarea에 입력되는 값들도 리액트에서 핸들링하도록 만들어준다.

textarea의 input을 핸들링할 state



삭제하기의 onClick 함수가 기니까 전역으로 빼준다.



수정하기를 누르면 표시되는 버튼들도 달라지게 한다.

> 삼항 연산자를 이용 `isEdit` state에 따라

```react
isEdit ? 
    <button>수정 취소<button/>
    <button>수정 완료</button>
    :
    <button>수정하기<button/>
    <button>삭제하기</button>
```



# 자주 등장하는 오류(부모 엘리먼트)

```
SyntaxError: D:\react-practice\simple-diary\src\DiaryItem.js: Adjacent JSX elements must be wrapped in an enclosing tag. Did you want a JSX fragment <>...</>? (33:12)
```

- 감싸고 있는 div가 분명히 있는데 왜 enclosing tag를 자꾸 요구할까?
- JSX elements의 범위가 어디야?
- 그냥 div일 땐 아무 오류가 안 났는데 조건문으로 랜더링하니까 (감싸지 않으면)저런 오류가 생긴다.

- 이전에 diartyLst도 그랬는데, 무슨 기준인지??