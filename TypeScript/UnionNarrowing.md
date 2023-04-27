# 3장. 유니언과 내로잉

- 유니언(*union*) :  값에 허용된 타입을 두 개 이상의 가능한 타입으로 확장하는 것
- 내로잉(*narrowing*) : 갑셍 허용된 타입이 *하나 이상의 가능한 타입이 되지 않도록* 좁히는 것



## 유니언(Union)

유니언 타입은 값이 정확히 어떤 타입인지 모르지만 두 개 이상의 옵션 중 하나라는 것을 알고 있는 경우 '이거 혹은 저거'와 같은 타입으로 추론되는 타입을 말한다.

### 유니언 타입 명시 방법

> 가능한 타입 사이에 `|`(수직선) 연산자를 사용하여 명시한다.

- 유니언 타입 선언

  ```typescript
  // 잠재적으로 null 대신 string이 될 수 있음
  * let thinker: string | null = null;
  
  if (Math.random() > 0.5) {
      // "Susanne Langer" = string
      thinker = "Susanne Langer";
  }
  ```

   * `thinker`의 초깃값은 `null`이지만 `thinker`의 값으로 <u>`string` 타입의 값을 할당할 수 있음</u>을 의미한다.

값이 유니언 타입일 때 타입스크립트는 유니언으로 선언한 타입 모두에 존재하는 멤버 속성에만 접근이 가능하다.

유니언 타입으로 정의된 여러 타입 중 하나의 타입으로 된 <u>값의 '속성'을 사용하려면 코드에서 값이 보다 구체적인 타입 중 하나라는 것</u>을 타입스크립트에 알려야 한다. 이를 '**내로잉**'이라고 한다.



## 내로잉(Narrowing)

> 값이 이전에 유추된 것보다 더 구체적인 타입임을 타입스크립트에 알리는 것

- 타입 가드(*type guard*) : 타입을 좁히는 데 사용할 수 있는 **논리적 검사**를 의미

### 내로잉 타입 가드

- 값 할당

  > 변수에 값을 직접 할당하여 변수의 타입을 할당된 값의 타입으로 좁히는 것

  ```typescript
  let admiral: number | string;
  
  // admiral 변수에 string 타입의 값을 할당함으로 admiral 변수가 string 타입임을 알림
  admiral = "Grace Hopper";
  
  adrmiral.toUpperCase();
  
  admiral.toFixed(); // Error 발생 : Property 'toFixed' does not exist on type 'string'.
  ```

  `string` 타입으로 내로잉되어 유추된 `admiral` 변수에 없는 멤버 `.toFixed()` 속성에 접근하려고 하면 오류가 발생한다.

  

- 조건 검사

  > `if`문 내에서 변수가 알려진 값과 동일한 타입인지 확인하는 것

  ```typescript
  let scientist = Math.random() > 0.5 ? "Rosalind Franklin" : 51;
  
  // 조건부 로직으로 내로잉
  * if (scientist === "Rosalind Franklin" {
      // scientist 변수: string
      scientist.toUpperCase();
      }
  
  ** scientist.toUpperCase(); // Error 발생 : Property 'toUpperCase' does not exist on type 'string | number'.
  // Property 'toUpperCase' does not exist on type 'number'.
  ```

  *`if`문 내에서 `string` 타입으로 내로잉된 `scientist` 변수의 `.toUpperCase()` 속성에 접근하는 것은 가능하지만, <br>**내로잉되지 않은 유니언 타입의 `. toUpperCase()` 속성에 접근하는 것은 `number` 타입에 해당 멤버 속성이 없기 때문에 오류가 발생한다.



- typeof 검사를 통한 내로잉

  > typerof 연산자를 사용할 수 있기 때문에 삼항 연산자를 이용할 수 있다.

  ```typescript
  typeof researcher === 'string' ?
      researcher.toUpperCase()
  	: researcher.toFixed();
  ```