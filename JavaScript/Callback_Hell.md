콜백 함수 안에서 콜백 함수를 부르고 부르고 부르고

콜백체인의 문제점

1. 읽기가 거북하다(가독성이 떨어짐)
2. 에러 발생이나 디버깅 시 너무 어렵다. 유지보수도 어려워진다.

어떻게 <u>병렬적으로 네트워크 통신</u>을 할 수 있을까?



## Callback Hell example

내가 만들고자 하는 것

```
1. 사용자에게 아이디, 비번을 받아서
2. 서버에 요청해서 성공적으로 로그인이 되면,
3. 받은 아이디로 다시 서버에 요청해서 성공적으로 이름과 역할(role)을 받아오면
4. 사용자에게 이름과 역할을 alert함.
```



서버에 요청하는 메서드를 가진 클래스 `UserStorage`를 생성

```javascript
class UserStorage {
    // 로그인 함수 : 아이디, 비밀번호, 성공 시 실행할 콜백, 실패 시 실행할 콜백
    loginUser(id, pwd, onSuccess, onError) {
        // 서버에 요청(서버가 없으므로 setTimeout 웹 API로 대체)
        setTimeout(() => {
            // 성공 시
            if ((id === 'avocado' && pwd === 'dream')||
                (id === 'coder' && pwd === 'academy'))
                {
                // 성공 콜백 실행
                onSuccess(id);                    
                } 
            // 실패 시
            else {
                // 실패 콜백 실행
                onError(new Error('not found'));
            }
        }, 2000);
    }
    
    // 이름과 역할 받아오는 함수 : 사용자, 성공 시 실행할 콜백, 실패 시 실행할 콜백
    getRoles(user, onSuccess, onError) {
        // 서버에 요청(서버가 없으므로 setTimeout 웹 API로 대체)
        setTimeout(() => {
            // 성공 시
            if (user === 'avoacado') {
                // 성공 콜백 실행
                onSuccess({name: 'avocado', role: 'admin'});
            }
            // 실패 시
            else {
                // 실패 콜백 실행
                onError(new Error('no access'));
            }
        }, 1000);
    }
}
```



### 1. 사용자에게 아이디, 비번을 받아서

새로운 인스턴스를 생성

```javascript
const userStorage = new UserStorage();
```

사용자에게 입력받은 아이디, 비번을 변수에 할당

```javascript
const id = prompt('enter your id');
const pwd = prompt('enter your password');
```



### 2. 서버에 요청해서 성공적으로 로그인이 되면 받은 아이디로 서버에 다시 요청해서 ~ 4. 사용자에게 이름과 역할을 alert함

```javascript
UserStorage.loginUser(
    id,
    pwd,
    // 성공 콜백: 성공하면 서버에 다시 요청
    // user 안에는 onSuccess에서 전달한 id 값('avocado')이 들어있음
    (user) => {
        UserStorage.getRoles(
            user,
            // 성공 콜백: 성공하면 이름과 역할을 alert
            // userWithRole 안에는 onSuccess에서 전달한 객체({name:'avocado', role: 'admin' })가 들어있음
            (userWithRole) => {
                alert(`Hello, ${userWithRole.name}, you have a ${userWithRole.role}`);
            },
            // 실패 콜백
            (error) => {
                console.log(error);
            }
        )
    }
)
```



## Promise

비동기를 간편하게 처리할 수 있도록 하는 object

비동기적인 것을 수행할 때 콜백함수 대신 사용할 수 있는 객체

Promise : executor를 실행하여 성공 시 콜백함수 resolve를 호출하고, 실패 시 콜백함수 reject를 호출하여 값을 전달하는 객체

