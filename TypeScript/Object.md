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