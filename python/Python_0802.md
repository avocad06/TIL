# 힙(Heap)

````
구성보다는 어떤 상황에서 활용할 수 있는지 컨셉을 이해하기
````

💡 일반적인 큐(Queue)는 순서를 기준으로 가장 먼저 들어온 데이터가 가장 먼저 나가는 선입선출 방식, <u>순서가 아닌 다른 기준으로는 ?</u>



- 우선순위 큐(Priority Queue)

> <u>우선순위(중요도, 크기 등 순서 이외의 기준)</u>를 기준으로 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식

- 우선순위 큐의 Use Case

  순서가 아닌 우선순위를 기준으로 가져올 요소를 결정하는 큐

  ````
  1. '가중치'가 있는 데이터
  2. 작업 스케줄링
  3. 네트워크
  ````

- 우선순위 큐를 구현하는 방법

1. 배열(Array)

2. 연결 리스트(Linkded List)

3. **힙(Heap)**

   

- 힙(Heap)

  우선순위 큐를 구현하는 방법 중 하나, 힙(Heap)이라는 데이터구조로 활용

  힙으로 우선순위 큐를 구현하면 시간복잡도가 **O(log N)**

  ````
  힙은 우선 순위 큐로 활용할 수 있는 데이터 구조
  ````

- 힙(Heap)의 특징

  최댓값 또는 최솟값을 빠르게 찾아내도록 만들어진 데이터구조

  <u>느슨한 정렬 상태를 지속적으로 유지한다</u>.

  

## Heap 의 Use Case
 > 1. 데이터가 지속적으로 정렬되어야 하는 경우(느슨하게라도 지속적으로 필요한 경우)
 > 2. 데이터에 삽입/삭제가 빈번할 때

  

- 파이썬의 `heqpq` 모듈

  파이썬이 직접 지원해주는 기능

  <u>Minheap(최소 힙)으로 구현되어 있음(가장 작은 값이 먼저 옴)</u>

  `heappop(heap)`기준은 여러 개로도 구현이 가능하다.

  ```python
  heapq.heqppop(abS(number), number)
  # 절댓값이 최우선순위, 실제 값이 우선순위
  # BOJ 11286
  ```

  **연산의 속도가 리스트보다 빠르다.**

  언제나 가장 작은 값/큰 값을 뽑아나갈 수 있도록(한 놈만 노린다)

  

- 힙과 리스트 비교

  | 연산 종류            | ✔힙(Heap)✔ | 리스트(List)                  |
  | -------------------- | ---------- | ----------------------------- |
  | 값 반환(Get Item)    | O(1)       | O(1)                          |
  | 값 삽입(Get Insert)  | O(logN)    | O(1) <append> / O(N) <insert> |
  | 값 삭제(Delete Item) | O(logN)    | O(1) <append> / O(N) <insert> |
  | 값 탐색(Search Item) | O(N)       | O(N)                          |
  
  

## Heap 구현
- 간단한 사용법 (**Python Tutor**)
  ```python
  import heapq # heapq 모듈 소환
  
  numbers = [5, 3, 2, 4, 1]
  
  heapq.heqpify(numbers) # numbers를 heap으로 형 변환
  
  # numbers 자체를 바꾸기 때문에 반환값이 없다.(원본 훼손하는 메소드)
  # result = heapq.heapify(numbers)
  print(result) # None 반환값이 없다.
  print(numbers)
  ==================================
  heapq.heappop(numbers) <Python Tutor>
  
  
  # 팝핑되자마자 다시 정렬됨.
  # 최소값은 맨 앞으로, 나머지 요소들은 나름의 규칙(랜덤은 아님)을 적용해서 정렬.
  ===================================
  import heapq # heapq 모듈 소환
  
  numbers = [3, 5, 2, 4, 1, 5]
  
  print(heapq.heappop(numbers))
  # 3
  # heap 형 변환을 하지않았기 때문에 그냥 맨 앞에 있는 값을 가져옴.
  
  heapq.heappush(numbers, 10)
  print(numbers)
  print(heapq.heappop(numbers))
  # [2, 5, 5, 4, 1, 10] # 내부 정렬이 일어나긴 함.
  # 2
  # 그냥 맨 앞 값을 가져옴.
  
  heapq.heappush(numbers, 0)
  print(numbers)
  # [0, 5, 2, 4, 1, 10, 5]
  # heappush가 되면서 자동으로 정렬
  
  ======================================
  import heapq
  
  numbers = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]
  
  heap = []
  # heapq.heapify(heap) 를 안 해도 됩니다.
  # heapq.heqppush 시점에 자동으로 정렬됨.
  # heapq.heappop(heap) 시점에서도 자동 정렬 될까?
  
  for number in numbers:
      if number != 0:
          heapq.heappush(heap, number)
      else:
          if len(heap) == 0:
              # len(heap) 으로 ==0 생략도 가능하다.(묵시적 형변환에 의한 불리언)
              print(0)
          else:
              print(heapq.heappop(heap))
  ```



## Heap 메소드

  1. `heapq.heapify(`) : 힙으로 형 변환, <u>**원본을 훼손**하는 메소드</u>(반환값이 x) 

  2. `heapq.heappush(heap, 인자)` : `인자`를 힙에 추가 

     상위 코드에서 `heapify()`로 **변환하지 않아도 최소 힙으로 정렬**하며 `인자`를 추가

3.  `heapq.heappop(heap)` : 힙에서 **최소값을** <u>반환하는 메소드</u>(반환값이 o)



# 셋(Set)

> 파이썬 내장 데이터 구조, '집합'을 나타내는 데이터 구조



## Set 연산

| 값 추가    | `.add()`    |
| ---------- | ----------- |
| 값 삭제    | `.remove()` |
| 셋과의 합  | `|`         |
| 셋과의 차  | `-`         |
| 교집합     | `&`         |
| 대칭차집합 | `^`         |



## Set의 Use Case

  > 1. 데이터의 **중복이 없어야 할 때**(고유값들로 이루어진 데이터가 필요할 때)
  > 2. **정수가 아닌 데이터**의 삽입/삭제/탐색이 빈번히 필요할 때

- 셋(`Set`) 연산의 시간 복잡도

  | 연산 종류   | 시간복잡도 |
  | ----------- | ---------- |
  | 탐색        | O(1)       |
  | 제거        | O(1)       |
  | 합집합      | O(N)       |
  | 교집합      | O(N)       |
  | 차집합      | O(N)       |
  | 대칭 차집합 | O(N)       |

​	✔ **탐색과 제거의 시간복잡도가 굉장히 낮다. 빠르다.** ✔ = 중복 없애기 쉽다.

```python
a = [1, 2, 3, 5]
b = [1, 7, 8, 9]
a, b = set(a), set(b)
print(a|b - b)
# {1, 2, 3, 5}
```



