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

  