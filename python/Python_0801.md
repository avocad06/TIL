# 코드리뷰

## 암호문

````
리스트로 값을 insert하기만 하면 삽입하고자 하는 인덱스의 값이 바뀌어서

역순으로 명령어를 받아온다? 한 번 역순 아닌 것도 진행해보자.
````

# 스택, 큐(Stack, Queue)

````
< 목 차 >
1. 스택
2. 큐
````

왜 데이터 구조가 중요한가?

💡 **문제 상황에 따라 더 적합한 통(도구)이 필요하기 때문에**

<u>문제를 더 효율적으로 풀기 위한 도구가 된다.</u>

데이터 구조&알고리즘

왜 써야 하는지(why)

데이터 구조를 배우는 이유 : **왜 만들어졌고, 언제 써야하는지 알기 위해서**

## 스택(Stack)

> 데이터를 한 쪽에서만 넣고 빼는 자료 구조

데이터가 한쪽에서만 넣고 빼는 자료구조이기 때문에, 가장 위에는 가장 최신 데이터, 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 <u>후입선출 방식</u> == 일반적인 '통'

- 스택 자료구조의 대표 동작

  **push** 스택에 새로운 데이터를 삽입하는 행위

  **pop** 스택의 가장 마지막 데이터를 가져오는 행위

- 왜 만들었을까?

  생각을 안하기 위해서, 가장 위에 있는게 가장 마지막 데이터야. 가장 최신 데이터야.

  💡 왜 한 쪽이 막혀있는 구조를 썼을까? ( Stack의 Use Case)

  1. **뒤집기, 되돌리기, 되돌아가기** ex) 인터넷 '뒤로가기', 'Ctrl + z ' 등

     <u>가장 마지막에 했던 액션이 가장 처음에 뜨도록</u>

     브라우저 히스토리, Ctrl + z, 단어 뒤집기

     

  2. **마무리 되지 않은 일을 임시 저장**

     다시 언젠가 찾아와야 하는 상황

     **괄호 매칭**(열렸는데 닫히지 않은 괄호를 찾는 것), 

     **함수 호출**(겹쳐 있는 함수 순차적 호출, 재귀호출), 

     ```python
     # 함수가 끝나지 않았는데 계속 호출해야하는 상황
     print(sum(max(min(2,5), 10), min(2,5)))의 call stack 과정
     print(sum(max(2, 10), min(2,5)))
     print(sum(10, min(2,5)))
     print(sum(10, 2))
     print(12)
     시작은 했는데 끝내지 못함.
     [print - sum - max - min- max- min- sum- print]
     ```
     
     백트래킹, DFS(깊이 우선 탐색) < 알고리즘 아직은 생각하지 말기 >
     
      

- 파이썬은 **리스트(List)로 스택을 간편하게** 사용할 수 있다!

- push, pop // 스택 자료구조를 따로 구현하지 않고 리스트를 사용한다.

  `.append()`, `.pop()` 

  |   push    |  pop   |
  | :-------: | :----: |
  | .append() | .pop() |

  ```python
  # BOJ 10773.제로
  # A) intput을 받아 input_list에 추가하고, 해당 리스트를 순회 및 숫자를 판별 하며 다른 리스트에 추가
  K = int(input())
  
  input_list = []
  
  for i in range(K):
      input_list.append(int(input()))
  
  stack = []
  
  for elem in input_list:
      if elem != 0:
          stack.append(elem)
      else:
          stack.pop()
          
  print(sum(stack))
  ==========================================
  # B) 'input을 받으면서' 해당 숫자를 판별하며 리스트에 추가
  stack = []
  for _ in range(int(input())):
      number = int(input())
      
      if number == 0:
          stack.pop()
      else:
          stack.append(number)
  print(sum(stack))
  ```

  아직까지는 A) 의 코드처럼 입력값을 다 저장하고 보면서 코드를 짜는 것이 좋다.

  
## 큐(queue)

> 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조

가장 먼저 들어온 데이터가 가장 먼저 나가므로 <u>선입선출 방식</u>

- 큐 자료구조도 파이썬 **List로 간편하게 사용** 가능하다!

  하지만 큐 안에 데이터가 많은 경우 비효율적

  맨 앞 데이터가 빠지면서, 리스트의 인덱스가 하나씩 당져지기 때문에

- pop(0)은 선형복잡도를 가지기 때문에 시간복잡도 역시 높다.



## 덱(Deque)

> 양 방향으로 삽입과 삭제가 자유로운 큐

- 덱(Deque, Double-Ended Queue) 자료구조

  == <u>양방향으로 삽입, 추출이 모두 큐보다 빠르다.</u>

  **from collections import deque**

  `range`나 `list`를 `deque`로 형 변환이 가능하다. 형 변환하여 사용한다.

  ```python
  from collections import deque
  
  numbers = [1, 2, 3, 4, 5]
  # 리스트를 덱스올 형 변환
  queue = deque(numbers)
  # 값을 추가할 때는 .append
  queue.append(6)
  # 인자없이 popleft() 순서 상관없이 맨 왼쪽 끝
  queue.popleft()
  
  print(queue)
  >>> deque([2, 3, 4, 5, 6])
  # 원하는 출력 형태에 따라 형 변환하여 출력
  ```

  