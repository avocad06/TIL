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