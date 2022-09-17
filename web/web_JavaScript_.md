# 변수와 식별자

식별자 : 변수를 구분할 수 있는 변수명

- 식별자는 반드시 문자, 달러 `$` 또는 밑줄 `_`로 시작
- <u>대소문자를 구분</u>하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능

- 한 줄에 두 개 이상의 명령문이 필요하다면 반드시 세미콜론 `;` 으로 구분

### 선언(Declarations)

> 변수를 생성하는 행위 또는 시점

| `var`   | 변수를 선언하며 추가로 동시에 값을 초기화<br>호이스팅 시 초기화되는 특성으로 인해 예기치 못한 문제 발생 가능 |
| ------- | ------------------------------------------------------------ |
| `let`   | 블록 스코프 지역 변수를 선언하며 추가로 동시에 값을 초기화<br>**<u>재할당 가능</u>** |
| `const` | 블록 스코프 **읽기 전용 상수**를 선언 <br><u>**상수 식별자**</u><br>**<u>재할당 불가능</u>** |

### 할당(Assignment)

> 선언된 변수에 값을 저장하는 행위 또는 시점

- 재할당

    ```js
    🚩 let은 재할당이 가능하지만, const 는 재할당이 불가능하다

    let number = 10;
    number = 20;
    console.log(number);
    20

    const number = 5;
    number = 10;
    // TypeError: Assignment to constant variable.
    // const 는 재할당이 불가능하므로 에러 발생
    ```

- 상수에 할당된 객체와 배열의 속성은 보호되지 않는다

  ```js
  🚩 배열의 내용과 객체의 속성을 바꿀 수 있다.
  
  
  const my_arr = ['html', 'css']; // 상수에 배열을 할당
  my_arr.push('js'); // 배열에 내용을 추가
  
  console.log(my_arr);
  (3) ['html', 'css', 'js'] // 성공적으로 내용 추가 가능
  
  
  const my_obj = {'key': 'val'}; // 상수에 객체를 할당
  my_obj.key = 'otherval'; // 객체의 key의 값을 변경
  
  console.log(my_obj['key']);
  otherval
  // 재할당으로는 값 변경이 안 되지만 객체의 속성은 변경
  ```

- 초기화(Initialization)

  선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

  `let`과 `var`는 변수를 선언함과 동시에 초기화를 한다.

    ```js
  let foo // 선언
  
  console.log(foo) // undefined
  undefined
  
  - 지정된 초기값 없이 `let`(혹은 var)문을 사용해서 선언된 변수는 `undefined`값을 갖는다.
    ```

- `let`과 `const` 모두 **재선언이 불가** 하지만 `var`는 가능하다.

  ```html
  let number = 10;
  let number = 50;
  
  SyntaxError: Identifier 'c' has already been declared
  ```

  



## 변수 스코프

- block scope

  > `let` `const` 는 블록 스코프

  **block** : `if` /`for`문, `function` 등의 <u>중괄호`{}`의 내부</u>

  블록 스코프를 가지는 변수는 블록 바깥에서 접근이 불가능하다

  ```js
  let x = 2; // x에 2를 선언 및 할당
  if (x === 2) {
      let x = 5; 
      console.log(x)
  } // x가 2라면 블록 스코프 내에서 x에 5를 재할당하고, 출력
  5 // 5
  
  console.log(x);
  2 // 블록 밖이므로 이전에 할당된 2를 출력
  ```

  ```js
  if (Math.random() > 0.5) {
      const y = 5; // 블록 스코프 생성
  }
  
  console.log(y);
  // ReferenceError: y is not defined
  // 블록 안에서만 변수 y가 존재
  ```

- function scope

  > `var`는 함수 스코프

  함수 스코프를 가지는 변수는 함수 바깥에서 접근이 불가능하다

  = `if`문, `for`문에서는 스코프의 제한을 받지않는다([not limited](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variable_scope))

  ```js
  🚩 if 문 밖에서의 함수 스코프 변수 접근: 가능
  
  var c = 6; // c를 선언 및 6을 할당
  
  if (true) {
      var c = 5;
  }
  console.log(c);
  5 // c의 스코프는 if 문 블록에 제한되지 않기 때문에 블록 밖에서 접근이 가능하다.
  ```

  ```js
  🚩 함수 밖에서의 함수 스코프 변수 접근: 불가능
  
  function foo() {
      var x = 5; } // 함수 내에서 x를 선언 및 5를 할당
  
  console.log(x);
  // ReferenceError: x is not defined
  // 함수 안에서만 변수 x가 존재
  ```

  

## 변수 호이스팅(hoisting)

> 나중에 선언된 변수를 참조할 수 있는 것

- 자바 스크립트는 모든 선언을 호이스팅한다.
- 끌어올려진 변수는 `undefined` 값을 반환
- `var`, `let`, `const` <u>모두 호이스팅이 발생하지만</u> <br>`var`는 호이스팅될 때 선언과 초기화가 동시에 발생하여 **일시적 사각지대**가 존재하지 않는다. (`let`**과** `const`**는** **초기화하지 않음**)

- let, const, var 비교

  | 키워드  | 재선언 | 재할당 |       스코프       |   비고   |
  | :-----: | :----: | :----: | :----------------: | :------: |
  |  `let`  |   X    |   O    | <u>블록 스코프</u> | ES6 도입 |
  | `const` |   X    |   X    | <u>블록 스코프</u> | ES6 도입 |
  |  `var`  |   O    |   O    |    함수 스코프     |  사용 X  |

  💡 결론: `let`과 `const`를 쓸 것



# 데이터 타입

> 원시타입과 참조타입으로 분류된다.

- 자바 스크립트의 모든 값은 특정한 데이터 타입을 가진다.

  | 원시 타입(Primitve type) | 참조 타입(Reverence type) |
  | ------------------------ | ------------------------- |
  |                          |                           |
  |                          |                           |
  |                          |                           |
  |                          |                           |
  |                          |                           |
  |                          |                           |
  |                          |                           |

  