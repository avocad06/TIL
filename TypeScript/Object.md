- 객체 타입 선언

  ```typescript
  let poetLater : {
      born: number;
      name: string;
  }
  
  poetLater= {
      born: 1935,
      name: "Mary Oliver"
  };
  
  poetLater = "Sappho" // Error : Type 'string' is not assignable to type '{born: number; name: string;}'
  ```

  객체 타입은 객체 리터럴과 유사하게 보이지만 필드 값 대신 타입을 사용해 설명한다.



- 객체 타입으로 애너테이션된 위치에 값을 제공할 때 타입스크립트는 값을 해당 객체 타입에 할당할 수 있는지 확인한다. 할당하는 값에는 객체 타입의 필수 속성이 있어야 한다. 객체 타입에 필요한 멤버가 객체가 없다면 타입스크립트는 타입 오류를 발생시킨다.

  ```typescript
  type TimeRange = {
      start: Date;
  };
  
  const hasStartString: TimeRange = {
      start: "1879-02-13", // Error : Type 'string' is not assignable to type 'Date'.
  }
  ```

  객체 타입은 필수 속성 이름과 해당 속성이 예상되는 타입을 모두 지정한다. 객체의 속성이 일치하지 않으면 타입스크립트는 타입 오류를 발생시킨다.

- 변수가 객체 타입으로 선언되고, 초깃값에 객체 타입에서 정의된 것보다 많은 필드가 있다면 타입스크립트에서 타입 오류가 발생한다. 하지만,

  ```typescript
  type Poet = {
      born: number;
      name: string;
  }
  
  *const existingObject = {
      activity: "Walking",
      born: 1935,
      name: "Mary Oliver",
  };
  
  **const extraPropertyButOk: Poet = existingObject;
  ```

  *에서 선언한 객체 리터럴 `existingObejct` 값을 **에서 할당하면, 타입 오류가 발생하지 않는다. 즉, 초과 속성 검사는 객체 타입으로 선언된 위치에서 생성되는 객체 리터럴에 대해서만 일어나고, 이미 존재하는 기존 객체 리터럴 값을 제공하면 오류가 발생하지 않는다.
  
- 변수에 여러 객체 타입 중 하나가 될 수 있는 초깃값이 주어지면 타입스크립트는 해당 타입을 객체 타입 유니언으로 유추한다. 객체 타입의 조합을 명시하는 방법은 다음과 같다.

  ```typescript
  type PoemWithPges = {
      name: string;
      pages: number;
  }
  
  type PoemWithRhymes = {
      name: string;
      rhymes: boolean;
  }
  
  type Poem = PoemWithPages | PoemWithRhymes;
  
  const poem: Poem = Math.random() > 0.5 ?
        {
            name: "The Double Image", pages: 7
        }:{
            name: "Her Kind", rhymes: true
        };
  
  poem.name;
  
  poem.pages; // Error : Property 'pages' does not exist on type 'Poem'. Property 'pages' does not exist on type 'PoemWithRhymes'
  ```

  변수의 유니언 타입과 같이 객체 타입 유니언도 모든 타입에 존재하지 않는 속성에만 접근할 수 있도록 오류를 발생시킨다.
  
- 타입 검사기가 유니언 타입 값에 특정 속성이 포함된 경우에만 코드 영역을 실행할 수 있음을 알게 되면, 값의 타입을 해당 속성을 포함하는 구성 요소로만 좁힌다. 즉, 코드에서 객체의 형태를 확인하고 타입 내로잉이 객체에 적용된다. 또한 타입스크립트는 존재하지 안흔 객체의 속성에 접근하려고 시도하면 타입 가드처럼 작동하는 방식으로 사용되더라도 타입 오류로 간주된다.

  ```typescript
  if ("pages" in poem) {
      poem.pages;
  } else {
      poem.rhymes;
  }
  ```

  타입스크립트는 `if (poem.pages)`와 같은 형식으로 참 여부를 확인하는 것을 허용하지 않는다.