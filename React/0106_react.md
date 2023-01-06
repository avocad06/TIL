다이어리 아이템마다 삭제버튼을 만들고, 삭제버튼을 누르면 해당 일기 데이터를 삭제하는 작업



삭제하기 버튼을 만들고 나서, id값이랑 어떻게 연결해줘야하지?

id값에 해당하는 아이템을 지워야 하니까, 연결을 해야 하는데 어떻게 연결하지?

=> 이미 연결이 되어 있음. => 왜? 부모 컴포넌트인 `DiaryList.js`의 `it.id`로 prop으로 보내주고 있기 때문에

```react
const DiaryItem = ({ author, content, created_at, emotion, 'id' })
```



`onclick`이벤트를 달아서 삭제하기를 누르면 함수가 실행되도록할 것.

```react
            <button onclick={() => {
                console.log(id);
            }}>삭제하기</button>
```

하지만 id값이 출력되지않음. => 잊지말자 리액트 `onClick` 속성 - `onclick` (x)



데이터 삭제 = 삭제하기를 누른 아이템을 뺀 배열로 `App.js`의 `data` state를 변경하는 것

`App.js`에서 `DiaryItem`으로부터 id값을 받아오는 함수를 만들어서 prop으로 보내고, 해당 id의 아이템을 뺀 배열로 `data`상태를 업데이트시키는 함수를 작성 (`onRemove()`)



`onRemove` 함수는 지우고자 하는 아이템을 눌렀을 때 <u>호출되며</u> 그 아이템의 id값을 받아와야 함.

=> `App.js`의 자식 컴포넌트`DiaryList`로 `onRemove`함수를 props로 전달하고,<br>다시 `DiaryList`의 자식 컴포넌트 `DiaryItem`으로 props로 전달해야 함.(`DiaryList`가 사용하지 않더라도 함수를 전달해야 하는 번거로움이 발생 = Prop Drilling이라고 한다) [Prop Drilling과 해결방법](https://slog.website/post/13)



전달받은 `onRemove`함수를 `DiaryItem`컴포넌트에서 호출하여 `App.js`의 매개변수 `targetId`에 지우고자 하는 아이템의 id 값을 전달



id값을 받아왔으므로 해당 id값을 가진 배열을 제외한 새로운 배열을 만들어서 `setData` 상태변화 함수의 인자로 전달해서 `data` state를 변화시킴.

