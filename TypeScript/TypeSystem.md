# 타입시스템

<br>

## 타입의 종류

- 타입 : 자바스크립트에서 다루는 값의 형태에 대한 설명
- 형태 : <u>*값에 존재하는 속성과 메서드*</u> 그리고 내장되어 있는 `typeof` 연산자가 설명하는 것을 의미

> 타입스크립트의 가장 기본적인 타입은 자바스크립트의 일곱 가지 기본 원시 타입과 동일하게 간주한다.

#### 일곱가지 원시 타입

| 자바스크립트 | 예시                | 타입스크립트 |
| ------------ | ------------------- | ------------ |
| `null`       | null;               | `null`       |
| `undefined`  | undefined;          | `undefined`  |
| `boolean`    | true;               | `boolean`    |
| `string`     | "Louise";           | `string`     |
| `number`     | 1337;               | `number`     |
| `bigint`     | 1337n;              | `bigint`     |
| `symbol`     | Symbol("Franklin"); | `symbol`     |

<hr>

타입스크립트는 계산된 초깃값을 갖는 변수의 타입을 유추할 수 있다.

```typescript
let bestSong = Math.random() > 0.5
? "Chain of Fools" : "Respect";
```

타입스크립트는 `bestSong`의 변수 타입을  `String`으로 유추한다.



### 타입 시스템

- **타입 시스템**(*TypeSystem*) : 프로그래밍 언어가 프로그램에서 가질 수 있는 타입을 이해하는 방법에 대한 <u>***규칙 집합***</u> 



타입 스크립트가 타입을 추론하는 과정

```typescript
let firstName = "Whitney";
firstName.length();

// This expression is not callable.      
// Type 'Number' has no call signatures.
```

위 코드는 타입스크립트가 멤버 속성을 함수로 잘못 호출해 타입오류가 발생하는 코드이다.

- 멤버 : 객체 혹은 클래스 내부에 정의된 함수를 멤버 함수, 변수를 멤버 변수



타입스크립트가 위 코드의 오류를 표시하는 순서는 다음과 같다.

1. 코드를 읽고 `firstName`이라는 변수를 이해
2. 초깃값이 `"Whitney"`이므로 `firstName`의 타입을 `string` 이라고 결정(유추)
3.  `firstName`의 `.length` 멤버를 함수처럼 호출하는 코드를 확인

4.  `string`의 `.lengh` 멤버는 함수가 아닌 숫자라는 표시 => 함수처럼 호출할 수 없음

> 타입스크립트는 변수의 초깃값에 따라 변수의 타입을 결정한다.



### 오류의 종류(타입오류/구문오류)

> 타입스크립트를 작성하며 가장 자주 접하게 되는 오류 두 가지

- 구문 오류 : 타입스크립트가 코드로 이해할 수 없는 *잘못된 '구문'을 감지할 때* 발생(타입스크립트가 자바스크립트로 변환되는 것을 차단)

- 타입 오류 : 타입스크립트의 타입 검사기가 프로그램의 *타입에서 오류를 감지했을 때* 발생

  타입스크립트는 타입 오류가 있어도 자바스크립트 코드를 출력할 수 있지만, 코드가 실행될 때 충돌 가능성이 있음을 타입 오류로 알려준다.



## 할당 가능성

> 타입스크립트는 변수의 초깃값을 읽고 해당 변수가 허용되는 타입을 결정한다.

- 할당 가능성(*assignability*) : 함수 호출이나 변수에 값을 제공할 수 있는지 <u>여부를 확인하는 것</u>

```typescript
let lastName = "King";
lastName = true;
```

타입스크립트 변수에 다른 타입의 값이 할당되면 **타입 오류가 발생**한다.

```typescript
// Type 'boolean' is not assignable to type 'string'.
```



```
*Type ... is not assignable to **type ...
```

*Type : 코드에서 변수에 할당하려고 시도하는 값(전달 된 값)

**type : 값이 할당되는 변수(예상된 타입)

*타입스크립트는 전달된 값이 예상된 타입으로 <u>할당 가능한지 여부</u>를 확인한다.*



## 타입 애너테이션

> 타입 애너테이션은 초깃값을 할당하지 않고도 변수의 타입을 선언할 수 있다.

- 진화하는 any : 초기타입을 유추할 수 없는 변수

타입스크립트는 기본적으로 변수를 암묵적인 `any` 타입으로 간주하기 때문에, 

초깃값이 할당되지 않아 타입스크립트가 허용되는 타입을 결정하지 않은 변수는 <u>*타입 검사 기능이 제대로 동작하지 않는다.*</u> 검사를 위해 알려진(유추된) 타입이 없기 때문이다.

- 타입 애너테이션(*annotation* : 주석) : 초깃값을 할당하지 않고도 변수의 타입을 선언할 수 있도록 타입스크립트가 제공하는 구문
  (자바스크립트로 컴파일되면 코드가 삭제되며 유효한 자바스크립트 구문도 아니고, 런타임 코드에 영향을 주지도 않는다.)
- 변수 이름 뒤에 콜론(`:`)과 타입 이름이 차례대로 기재된다.

```typescript
let rocker: string;
rocker = "Joan Jett";
```

타입 애너테이션은 변수에 초깃값이 할당되지 않아 <u>타입을 유추할 수 없어</u> 타입스크립트가 <u>*자체적으로 수집할 수 없는 정보를 타입스크립트에 제공하여*</u> 진화하는 any 를 방지한다.

<hr>

타입 애너테이션은 초기 타입을 즉시 유추할 수 있는 변수에도 사용할 수 있다.

초기 값이 있는 변수에 타입 애너테이션을 추가하면 타입스크립트는 변수에 할당된 값의 타입이 일치하는지 확인한다.

```typescript
let firstName: string = 42;
```

타입애너테이션으로 정의한 타입이 우선된다.

```typescript
// Type 'number' is not assignable to type 'string'.
```



## 타입 형태

> 타입스크립트는 접근하려는 속성이 해당 변수의 타입에 존재하는지 확인한다.

```typescript
let cher = {
    firstName: "Cherilyn",
    lastName: "Sarkisian",
};
```

`cher` 객체에 `middleName` 키가 없다는 것을 알고 오류를 표시한다.

```typescript
// Property 'middleName' does not exist on type 
'{ firstName: string; lastName: string; }'.
```

타입스크립트는 객체의 형태에 대한 이해를 바탕으로 할당 가능성 뿐만 아니라 객체 사용과 관련된 문제도 알려준다.





