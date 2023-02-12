# Suspense

[`React-Suspense`]([React Suspense 소개 (feat. React v18) | Engineering Blog by Dale Seo](https://www.daleseo.com/react-suspense/))

> 컴포넌트를 Suspense로 감싸주면 컴포넌트의 랜더링을 특정 작업 이후로 미루고, 작업이 끝날 때까지 `fallback`속성으로 넘긴 컴포넌트를 대신 보여줄 수 있다.

- API 를 호출하여 비동기로 데이터를 가져오는 코드를 분리

`function fetchUser(userId)` : 데이터를 서버로부터 받아서 3초 뒤에 user에 data를 바운딩하는 함수

```react
function fetchUser(userId) {
  let user = null;
  const suspender = fetch(
    `https://jsonplaceholder.typicode.com/users/${userId}`
  )
    .then((response) => response.json())
    .then((data) => {
      setTimeout(() => {
        user = data;
      }, 3000);
    });
```



```react
 return {
    read() {
      if (user === null) {
        throw suspender;
      } else {
        return user;
      }
    }
  };
```

user가 null일 때(데이터 수신 중)는 `suspender`를 반환하고, 받아온 data가 user에 바운딩 되면(수신 완료) user를 반환하는 함수 => `read()`<u>함수를 반환</u>한다.

`User.js`

최상위 컴포넌트에서 호출한 함수의 return값을 prop으로 전달

=> 최상위 컴포넌트가 랜더링될 때 fetchData가 호출(불필요한 useEffect안 써도 된다.)

최상위 컴포넌트가 호출한 함수는 함수를 반환한다.

(어느 데이터를 가져오는 함수를 호출할지.)

`User`의 자식 컴포넌트인 `Post`도 데이터를 가져오기 전까지 fallback 속성에 전달된 컴포넌트를 랜더링한다.(하지만 아직 부모 컴포넌트 `User`가 대기 중이라면 User의 fallback컴포넌트가 랜더링 중일 것이므로 Post는 볼 수가 없다. Post가 값을 먼저 불러와도 중구난방으로 화면에 렌더링될 걱정을 하지 않아도 된다.) => 두 비동기 요청 컴포넌트가 거의 동시에 화면에 나타나는 것을 볼 수 있다.

```react

```