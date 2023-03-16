

# 옵셔널체이닝 `?.` option-chaining

> 프로퍼티가 없는 중첩 객체를 에러없이 안전하게 접근할 수 있다.



## 옵셔널 체이닝의 등장 배경

1. 사용자가 여러 명이 있는데 그 중 몇 명은 주소 정보를 가지고 있지 않아 주소 프로퍼티에 접근하려고 하면 에러가 발생

   ```javascript
   let user = {}; // 주소 정보가 없는 사용자
   
   alert(user.address.street); // TypeError: Cannot read property 'street' of undefined
   ```

2. 자바스크립트를 사용해 페이지에 존재하지 않는 요소에 접근해 요소의 정보를 가져오려고 하면 문제가 발생

   ```javascript
   // querySelector(...) 호출 결과가 null인 경우 에러 발생
   let html = document.querySelector('.my-element').innerHTML;
   ```

   

### 이전에는

> `&&` 연산자를 사용하여 해결했다.

```javascript
let user = {}; // 주소 정보가 없는 사용자

alert( user && user.address && user.address.street ); // undefined, 에러가 발생하지 않습니다.
```

- user가 있으면, address를, address까지 있으면 street까지 접근하도록 실제 해당 객체나 프로퍼티가 있는지 확인하는 방법을 사용



## 옵셔널 체이닝의 등장

>  '앞'의 평가 대상이 `undefined`이거나 `null`이면 평가를 멈추고 *`undefined`*를 반환

- 1의 상황(: 주소 프로퍼티가 없는 사용자의 주소에 접근하는 경우) 안전하게 접근하기

  ```javascript
  let user = {}; // 주소 정보가 없는 사용자
  
  alert( user?.address?.street ); // undefined, 에러가 발생하지 않습니다.
  ```

  `user?.address?.street` 으로 `user`객체가 있는지, 있다면 `address`라는 프로퍼티가 있는지 확인하며 접근

  

  ✔ `user?.address`는 `user`객체가 존재하지 않더라도 에러가 발생하지 않음

  ```javascript
  let user = null; // user는 null
  
  alert( user?.address ); // undefined: user가 있는지 확인 => 존재하지 않으므로 바로 undefined 반환
  alert( user?.address.street ); // undefined
  ```

  `user`객체가 존재하는지의 평가에서 바로 `undefined`가 반환되기 때문에, 존재하지 않는 프로퍼티에 접근하려고 해도 에러를 발생시키지 않음.

  👉 <u>*'앞'에 있는 평가 대상에만 동작한다!*</u>

  + 만약 `user`가 `null`이나 `undefined`이 아닌 실제 값이 존재했다면, `address` 프로퍼티에 대한 평가 로직이 없기 때문에 에러가 발생할 것. => `user?.address?.street`이 되어야 에러 발생 ❌



## ⚠ 주의사항

🤔 `?.`은 <u>존재하지 않아도 괜찮은 대상에만</u> 사용해야 한다.

사용자 주소를 다루는 예시에 경우 논리상 `user`는 반드시 있어야 하지만, `address`는 필수 값이 아니기 때문에 `user.address?.street`으로 사용하는 것이 바람직하다.



🤔 `?.`의 앞에 있는 변수는 꼭 선언되어 있어야 한다. 변수 `user`가 선언되어 있지 않으면 `user?.anything`평가 시 에러가 발생한다.

```javascript
// ReferenceError: user is not defined
user?.address;
```

`user?.anything`을 사용하려면 `let`이나 `const`, `var` 를 사용해 `user`를 꼭 정의해야 하고, 정의돼 있어야 한다.

*옵셔널 체이닝은 선언이 완료된 변수를 대상으로만 동작한다.*