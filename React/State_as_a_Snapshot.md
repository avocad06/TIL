# useState사용 시 주의사항

상태 변수의 값은 변하지 않는다.

setState()를 호출할 때 re-render를 트리거하고, snapshot으로 찍어서 변수의 값이나 prop 등의 변수의 값은 고정된다. 업데이트 대기열은 이벤트 핸들러의 실행이 끝나고 리렌더될 때 실행되고, 변경하고자 하는 값을 넣으면 업데이트 대기열은 변경하고자 하는 값으로 '대체'하는 식으로 실행된다. 변수는 고정되어 있으므로 순차적으로 state setter를 작성했더라도 같은 결과가 반환된다. 한편, 함수는 이전의 state를 받아와 새로운 값을 '반환'하므로 순차적으로 업데이트된 변수의 값을 얻어서 연산할 수 있다.



# State as a Snapshot

State는 읽고 쓸 수 있는 일반 JavaScript 변수처럼 보일 수 있지만, State는 스냅샷처럼 동작한다. State 변수를 설정해도 *이미 가지고 있는 State <u>변수가 변경되는 것이 아니라 re-render을 trigger</u>한다.*

- 상태를 <u>설정한 직후 상태가 업데이트되지 않는 이유</u>
- 이벤트 핸들러가 상태의 '스냅샷'에 액세스하는 방법



## Setting state triggers renders

> 상태를 설정하는 것은 리렌더를 트리거한다.

사용자가 클릭을 하면 인터페이스가 직접 변경된다고 생각하지만, state가 React에 다시 렌더링을 요청하는 방식이다. 즉, 인터페이스가 이벤트에 반응하려면 state를 업데이트해야 한다.

[이 예제](https://react.dev/learn/state-as-a-snapshot#setting-state-triggers-renders)에서 사용자가 버튼을 클릭하면 다음과 같은 일이 발생한다.

```react
import { useState } from 'react';

export default function Form() {
  const [isSent, setIsSent] = useState(false);
  const [message, setMessage] = useState('Hi!');
  if (isSent) {
    return <h1>Your message is on its way!</h1>
  }
  return (
    <form onSubmit={(e) => {
      e.preventDefault();
      setIsSent(true);
      sendMessage(message);
    }}>
      <textarea
        placeholder="Message"
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
      <button type="submit">Send</button>
    </form>
  );
}

function sendMessage(message) {
  // ...
}
```

1. `onSubmit` 이벤트 핸들러가 실행된다.
2. `sentIsSent(true)`는 `isSent` state를 `true`로 설정하고, <u>새 렌더링을 대기열에 추가한다.</u>
3. React는 새로운 `isSent` state 값에 따라 컴포넌트를 다시 렌더링한다.



state와 rendering의 관계를 더 자세히 살펴보자.

## Rendering takes a snapshot in time

> 렌더링은 ''스냅샷''을 찍는다.

'렌더링'이란 React가 컴포넌트, 즉 함수를 **호출**한다는 의미이다. 해당 함수가 반환하는 JSX는 시간상 UI의 스냅샷과 같다. **props, 이벤트 핸들러, 로컬 변수**들이 모두 렌더링 당시의 상태를 사용해 계산된다.

사진이나 영화 프레임과는 달리 UI 'snapshot'은 동적이다. 여기에는 입력에 대한 응답으로 어떤 일이 일어날지 지정하는 이벤트 핸들러와 같은 로직들이 포함된다. React는 <u>이 스냅샷에 맞춰 화면을 업데이트하고 이벤트 핸들러를 연결한다</u>. 결과적으로, 버튼을 누르면 JSX에서 클릭 핸들러가 trigger된다.

React는 다음과 같이 리렌더한다.

1. React가 함수를 '다시' 호출한다.
2. 함수는 **<u>새로운 JSX 스냅샷을 반환</u>**하고,
3. React는 반환된 스냅샷과 일치하도록 화면을 업데이트한다.



컴포넌트 메모리로서, state는 일반 변수처럼 함수가 반환된 후에도 사라지지 않는다. state는 실제 함수 외부에, React자체에 존재한다. React가 컴포넌트를 호출하면 **특정 렌더링에 대한 state의 스냅샷**을 제공한다. 컴포넌트는 해당 렌더링의 state 값을 사용해 계산된 **새로운 props와 이벤트 핸들러가 포함된 UI의 스냅샷을 JSX에 반환**한다.



[다음 예제](https://react.dev/learn/state-as-a-snapshot#rendering-takes-a-snapshot-in-time)에서 우리는 다음 렌더링에 `number` state 값이 `3`이 될 것이라고 예상한다.

```react
import { useState } from 'react';

export default function Counter() {
  const [number, setNumber] = useState(0);

  return (
    <>
      <h1>{number}</h1>
      <button onClick={() => {
        // setNumber을 3번 호출했으므로 3이 될 것이라 예상
        setNumber(number + 1);
        setNumber(number + 1);
        setNumber(number + 1);
      }}>+3</button>
    </>
  )
}
```

하지만, 버튼을 누를 때마다 `+3`이 아닌 `+1`씩 증가하는 것을 볼 수 있다.

state를 설정하는 것은 다음 렌더링에서만 변경되기 때문이다. 첫 번째 렌더링에서 `number` state의 값은 `0`이었기 때문에, <u>해당 렌더에서의 이벤트 핸들러에서 여전히 `number` state의 값은 `0`으로 고정된다.</u>

앞서 작성한 state setter는 

```react
setNumber(number + 1);
setNumber(number + 1);
setNumber(number + 1);
```

같은 렌더링 내의 이벤트 핸들러에서 `number` state의 값이 `0`으로 고정됨에 따라 다음과 같이 동작한 것이다.

```react
setNumber(0 + 1);
setNumber(0 + 1);
setNumber(0 + 1);
```

렌더링의 이벤트핸들러당 고정된 변수에 `+1`씩 추가하도록 동작하므로 다음 렌더링에서도 `+1`씩 렌더링되어 우리가 예상한 `+3`이 아니라 `+1`씩 증가하는 화면을 볼 수 있다.



## State over time

> 렌더링당 고정된 state의 값은 변하지 않는다.

React에 저장된 state 값은 *사용자가 상호작용한 시점의 state snapshot을 사용*하여 예약된다.

state 변수의 값은 이벤트 핸들러의 코드가 비동기적이더라도 같은 렌더링 내에서 절대 변경되지 않는다. 

```react
import { useState } from 'react';

export default function Counter() {
  const [number, setNumber] = useState(0);

  return (
    <>
      <h1>{number}</h1>
      <button onClick={() => {
        setNumber(number + 5);
        // 비동기로 3초 뒤 number 값 alert하도록 실행
        setTimeout(() => {
          alert(number);
        }, 3000);
      }}>+5</button>
    </>
  )
}
```

[위 코드](https://react.dev/learn/state-as-a-snapshot#state-over-time)의 실행결과 여전히 `0`이 alert된다. aelrt가 실행될 때 React의 저장된 state는 변경되었을 수도 있지만, snapshot은 사용자가 상호작용한 시점(버튼 클릭)의 것으로 사용되기 때문이다. 즉, `number` state의 값이 `0`인 렌더의 UI 스냅샷이 사용되었다.

해당 렌더의 `onClick` 내에서, `setNumber(number + 5)`가 호출된 후에도 `number`의 값은 계속 `0`이다. 이 값은 <u>React가 컴포넌트를 호출해 **UI의  스냅샷을 가져올 때 고정된 값**</u>이다. 

React는 하나의 렌더링 이벤트 핸들러 내에서 state의 값을 '고정'으로 유지한다.



# Queueing a Series of State Updates

> 일련의 상태 업데이트 대기열에 대기

state 변수를 설정하면 대기열에 새로운 렌더링이 추가된다. 하지만 우린 때로 다음 렌더링을 대기열에 추가하기 전에 값에 대해 연산 등을 추가하고 싶을 수 있다. 이를 위해서는 React가 state 업데이트를 어떻게 일괄처리(**batch**es)하는지 알면 도움이 된다.

- batching(일괄 처리)란 무엇이며 React가 이를 사용하여 여러 state 업데이트를 처리하는 방법
- 동일한 state 변수에 여러 업데이트를 연속으로 적용하는 방법



## React batches state updates

> React는 이벤트 핸들러 안의 state를 일괄처리하여 업데이트한다.

React는 state 업데이트를 처리하기 전에 이벤트 핸들러의 모든 코드가 실행될 때까지 기다린다. 지금까지 봤던 예제에서 state setter를 여러 번 작성하여 호출해도 한 번 호출한 것처럼 작동한 이유가 이것이다. 이벤트 핸들러의 모든 `setNumber()` 호출이 끝난 다음에 리렌더링이 일어났기 때문이다.

이렇게 하면 여러 컴포넌트에서 여러 state 변수를 업데이트해도 너무 많은 리렌더링을 트리거하지 않고 업데이트할 수 있게 된다. 하지만 이는 곧 *이벤트 핸들러와 그 안에 있는 코드가 완료될 때까지는 UI가 업데이트되지 않는다*는 의미이기도 하다.

**batching**(일괄처리)은 React 앱을 훨씬 빠르게 실행할 수 있게 해주고, 일부 state 변수만 업데이트가 일어난 시점에서 렌더링되지 않도록 state 업데이트의 안정성을 강화한다.



## Updating the same state multiple times before the next render

> state setter에 업데이터 함수를 제공하면 최종 state 변수의 값으로 'doing something'할 수 있다.

흔히 사용되는 경우는 아니지만, 같은 state 변수를 다음 렌더링 전에 여러 번 업데이트하기 원한다면 변경하고자 하는 값을 바로 전달하는 것이 아니라 함수를 전달할 수 있다. 이 함수는 대기열에서 이전의 값을 기반으로 다음 state 변수의 값을 계산하는 형태로, `setNumber(n => n + 1)` 처럼 사용할 수 있다.

즉, 변경하고자 하는 값으로 단순히 대체하는 대신 state 값으로 'do something'하라고 지시하는 방법이다.

[이 예제](https://react.dev/learn/queueing-a-series-of-state-updates#updating-the-same-state-multiple-times-before-the-next-render)는 우리가 기대한 것처럼 클릭 한번에 `+3`을 해준다.

```react
import { useState } from 'react';

export default function Counter() {
  const [number, setNumber] = useState(0);

  return (
    <>
      <h1>{number}</h1>
      <button onClick={() => {
        // 다음 state 값 대신 업데이터 함수를 전달
        setNumber(n => n + 1);
        setNumber(n => n + 1);
        setNumber(n => n + 1);
      }}>+3</button>
    </>
  )
}
```

여기서 `n => n + 1`을 업데이터 함수라고 한다.

업데이터 함수가  세 번 작성되었으므로, 대기열에는 다음과 같이 추가된다.

```
`setNumber(n => n + 1)` : `n => n + 1` 은 함수이다. 대기열에 추가
`setNumber(n => n + 1)` : `n => n + 1` 은 함수이다. 대기열에 추가
`setNumber(n => n + 1)` : `n => n + 1` 은 함수이다. 대기열에 추가
```

즉, 3개의 업데이터 함수가 대기열에 추가된다.

1. React는 이벤트 핸들러의 다른 모든 코드가 실행된 후에 이 함수가 처리되도록 대기열에 추가한다.
2. 다음 렌더링 중에, React는 대기열을 통과하여 최종 업데이트된 state 값을 제공한다.

*다음 렌더링 중에 `useState()`를 호출*하면 React는 대기열을 처리한다. 

이전 `number` state 변수의 값은 `0`이었으므로, React는  `0`을  첫 번째 업데이터 함수에 함수의  `n`인자로 전달한다.(첫 번째 업데이터 함수의 인수로 `0`이 전달되어 호출) 다음 대기열에서 React는 이전 업데이터 함수(첫 번째 업데이터 함수)의 반환값을 가져와서 다음 업데이터(두 번째 업데이터 함수)의 인자로 전달하는 방식으로 진행된다.

| queued update | `n`  | returns     |
| ------------- | ---- | ----------- |
| `n => n + 1`  | `0`  | `0 + 1 = 1` |
| `n => n + 1`  | `1`  | `1 + 1 = 2` |
| `n => n + 1`  | `2`  | `2 + 1 = 3` |

위와 같은 대기열을 거쳐 React는 `3`을 최종 결과로 저장하고, `useState()`의 반환값으로 제공한다.

즉, 최종 state의 값을 `3`으로 인식하여 이전처럼 `1`이 아닌 한 번에 `3`씩 증가하는 UI를 출력한다.



## What happens if you update state after replacing it

> 'replace'와 'doing something'은 다르게 대기열에 추가된다.

- [update state after replacing it](https://react.dev/learn/queueing-a-series-of-state-updates#what-happens-if-you-update-state-after-replacing-it) : state 변수를 reaplce한 후에 업데이트했을 경우

  ```react
  import { useState } from 'react';
  
  export default function Counter() {
    const [number, setNumber] = useState(0);
  
    return (
      <>
        <h1>{number}</h1>
        <button onClick={() => {
          setNumber(number + 5);
          setNumber(n => n + 1);
        }}>Increase the number</button>
      </>
    )
  }
  ```

  `onClick` 이벤트 핸들러는 React에게 다음과 같이 지시한다.

  1. `setNumber(number + 5)` : `number`는 `0`이므로 `setNumber(0 + 5)`이다.

     React는 `'replace with 5'`를 대기열에 추가한다. 

  2. `setNumber(n => n + 1)` : `n => n + 1` 은 업데이터 함수다.

     React는 함수를 대기열에 추가한다. 

  *다음 렌더링 중*에, React는 다음과 같이 대기열을 처리한다.

  | queued update    | `n`                                                          | returns     |
  | ---------------- | ------------------------------------------------------------ | ----------- |
  | replace with `5` | `0` (이지만 실제 값이 사용되지 않음 <br>= state 변수를 사용하여 'doing something' 하지 않았음) | `5`         |
  | `n => n + 1`     | `5` (이전의 반환값 `5`)                                      | `5 + 1 = 6` |

  React는 `6`을 최종 결과로 저장하고, 다음 렌더링의 `useState()`호출의 반환값으로 제공한다.

- [reaplce state after updating it](https://react.dev/learn/queueing-a-series-of-state-updates#what-happens-if-you-replace-state-after-updating-it) : state 변수를 업데이트한 후에 reaplce했을 경우

  ```react
  <button onClick={() => {
    setNumber(number + 5);
    setNumber(n => n + 1);
    setNumber(42);
  }}>
  ```

  1. `setNumber(number + 5)` : `number`는 `0`이므로 `setNumber(0 + 5)`이다.

     React는 `'replace with 5'`를 대기열에 추가한다. 

  2. `setNumber(n => n + 1)` : `n => n + 1` 은 업데이터 함수다.

     React는 함수를 대기열에 추가한다. 

  3. `setNumber(42)` : React는 'replace with `42`'를 대기열에 추가한다.

  *다음 렌더링 중*에, React는 다음과 같이 대기열을 처리한다.

  | queued update     | `n`                                                          | returns     |
  | ----------------- | ------------------------------------------------------------ | ----------- |
  | replace with `5`  | `0` (이지만 실제 값이 사용되지 않음 <br>= state 변수를 사용하여 'doing something' 하지 않았음) | `5`         |
  | `n => n + 1`      | `5` (이전의 반환값 `5`)                                      | `5 + 1 = 6` |
  | reaplce with `42` | `6`(사용되지 않음)                                           | `42`        |

  React는 `42`을 최종 결과로 저장하고, 다음 렌더링의 `useState()`호출의 반환값으로 제공한다.



위 두 사례를 통해 보았을 때, 업데이터 함수와 값을 바로 넣는 것은 대기열에 다르게 추가되어 반환된다는 것을 알 수 있다.

> state setter에 함수를 전달하면, 업데이터 함수는 대기열에 추가된다.

> state setter에 값을 전달하면, 이전 대기열의 반환 값과 상관없이 값으로 대체된다.
