자바스크립트에서 초깃갑싱 없는 변수는 기본적으로 `undefined`가 된다. 타입스크립트는 값이 할당될 때까지 변수가 `undefined`임을 충분히 이해한다.

값이 할당되기 전에 속성에 접근하려는 등 해당 변수를 사용하려고 하면 오류가 발생한다. 아무리 옵셔널체이닝으로 값이 있는지 없는지 평가해도 오류가 발생한다.

```typescript
let mathmatician: string;

mathmatician?.length; // Error : Variable 'mathmatician' is used before being assigned.

mathmatician = "Mark Goldeberg";
mathmatician.length;
```



변수 타입에 `undefined`를 포함시키면 오류가 발생하지 않는다.

```typescript
let mathmatician: string | undefined;

mathmatician?.length; // 오류가 발생하지 않는다.

mathmatician = "Mark Goldberg"
```

`undefined`를 포함시키면 사용 전에는 정의할 필요가 없음을 나타내면서 유효한 타입임을 타입스크립트에 알릴 수 있다.