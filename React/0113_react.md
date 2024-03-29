React 컴포넌트의 생애 주기(생명 주기)

- 탄생 : 화면에 나타나는 것 `Mount`

- 변화 : 업데이트(리렌더링) `Update`

- 죽음 : 화면에서 사라짐 `UnMount`



컴포넌트의 LifeCycle을 제어한다는 것 => 컴포넌트의 탄생, 변화, 죽음 시점에 어떤 작업을 수행시킬 수 있다는 것

ex) Mount 시 초기화, Update시 예외 처리, UnMount시 메모리 정리 및 반환 작업 등을 수행하게 할 수 있다.



리액트는 생애주기별 사용할 수 있는 메서드가 따로 존재한다.

원래는 클래스형 컴포넌트에서만 사용할 수 있었지만, 리액트 훅으로 가능해졌다.

`React Hooks`

useState, useEffect, useRef . . .etc



함수형 컴포넌트를 사용하는 이유 : 클래스형 컴포넌트는 함수형 컴포넌트보다 복잡하고, 중복 코드를 많이 써야 하기 때문에 <u>가독성이</u> <u>떨어짐</u>



```
useEffect(Callback 함수, [의존성 배열])
```

> 배열 내에 들어있는 값이 변화하면 콜백 함수가 수행된다.



실험용 컴포넌트 생성 후 App.js에 import

1. Mount 되는 시점 제어하기 : 마운트 되는 시점에 `Mount!`출력하기 

   ```react
   import {useEffect} from 'react'
   
   // 첫 번째 매개변수는 콜백함수, 두 번째 매개변수는 빈 배열(depth)
   // dependency array가 빈 배열이므로 마운트되는 시점에만 콜백함수 실행
   useEffect( ()=>{
       console.log('Mount!');
   }, []);
   ```

   ```
   그런데! 강의에서는 `Mount!`가 1번 찍혔는데 난 왜 두 번 찍힐까?
   
   => ?
   ```

   - 마운트 되는 시점에서만 콜백함수가 실행되기 때문에(depth가 빈 배열이므로) count나 text의 state가 변화해도 더 이상 콜백함수는 실행되지 않는다.

     

2. Update 되는 시점 제어하기 : 업데이트 되는 시점에 `Update!` 출력하기

   > 컴포넌트가 업데이트 되는 시점(리렌더링)
   >
   > - state 가 변경되거나
   > - 부모 컴포넌트가 리렌더링되거나
   > - 부모 컴포넌트로부터 전달받은 props가 변경되거나

   ```react
   // 대상에 상관없이 업데이트 시점을 제어하려면 매개변수에 배열(depth)을 전달하지 않으면 된다.
   useEffect(()=>{
       console.log('Update!');
   });
   ```

   - dependency array(depth)에 넣는 값에 따라 감지하고 싶은 대상만 감지할 수 있게 됨.(count만 update 될 때, text만 업데이트 될 때)

     `count`

     ```react
     useEffect(() => {
             console.log(`count is update:${count}`)
         }, [count])
     ```

     `text`

     ```react
     useEffect(() => {
             console.log(`text is update: ${text}`)
         }, [text])
     ```

   - 업데이트되는 시점에 동작을 제어할 수 있음. (count가 5를 넘었을 경우 이를 감지하여 1로 초기화하는 콜백 함수)

     ```react
     useEffect(() => {
             if (count > 5) {
                 alert("count가 5를 넘었습니다. 1로 초기화합니다.")
                 setCount(1)
             }
         }, [count])
     ```

   - 단락회로 평가를 이용하면 컴포넌트의 렌더링을 제어할 수 있다.

     ```react
     {isVisible && <UnmountTest/>}
     ```

     `isVisible`이 true이면 `UnmountTest`를 렌더링하고, false이면 렌더링하지않음.

     

3. Unmount되는 시점 제어하기 : Mount되는 시점에 실행되는 콜백함수에 Unmount 시점에 실행되게 할 콜백함수를 전달

   ```react
   const UnmountTest = () => {
   
       useEffect(() => {
           console.log("Mount!")
           return () => {
               // Unmount 시점에 실행될 콜백함수
               console.log("Unmount!")
           }
       }, [])
   ```



=> `useEffect()`를 이용하면 , Mount/Update/Unmount 되는 시점 제어와 특정 값의 변화를 추적할 수 있다.
