# 코드리뷰

````
1. 절댓값 힙
2. 인사성 밝은 곰곰이
````

- 절댓값 힙

  ````
  heap의 요소에는 리스트를 넣을 수도 있다.
  리스트가 요소일 경우 내장 리스트의 인덱스 순서로 heapq가 적용된다.
  ex) [[0, 0, 3], [0, 0, -2]]
  앞의 인덱스 값들은 0, 0 으로 동일하므로 [2]의 값으로 둘 중 최소값이 정해진다.
  ````

- 인사성 밝은 곰곰이

  ````
  set은 중복을 탐색하는 데에 효과적이다.
  list를 탐색하는 복잡도는 O(N)이지만,
  set을 탐색하는 복잡도는 O(1)이다.
  ````

  

# 이차원 리스트

````
< 목 차 >
1. 이차원 리스트
2. 
````

왜 행렬이 중요할까? 현실의 데이터를 표현하기 위해서

## 이차원 리스트

> 리스트를 원소로 가지는 리스트일 뿐.

```python
matrix = [[1, 2,3], [4, 5, 6], [7, 8, 9]]
```

인덱싱을 2번하는 형태로 내장된 리스트의 요소 조회가 가능

- 그러면 **순회**를 어떻게 하지 ?

- 특정값으로 <u>초기화된 이차원 리스트</u> 만들기

  1. 직접작성 100 * 100 이라면?

  2. 반복문으로 작성( 100 * 100)

     ```python
     print([0] * 10)
     matrix = []
     for _ in range(10):
         matrix.append([0] * 10)
     print(matrix)
     ```

      n * m 

     n은 행의 개수

     m은 열의 개수

     반복문의 범위는 행렬의 높이를 결정.

  3. 리스트 컴프리헨션으로 작성

     ```python
     matrix = [앞 조건/반복]
     [[0] * 10 for _ in range(10)]
     
     ```

     💡 **리스트 컴프리헨션** vs 리스트 곱셉 연산

     ```python
     n = 3
     m = 3
     # 리스트 컴프리헨션
     matrix1 = [[0] * m for _ in range(n)]
     
     print(matrix1)
     >> [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
     
     # 리스트의 곱셉 연산
     matrix2 = [[0] * m] * n
     # [[0] * m >>> [[0, 0, 0]]
     print(matrix2)
     >> [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # 출력값은 같아 보인다.
     ```

     출력값은 같아 보이지만, 인덱스에 접근해서 리스트의 요소값을 변경할 경우

     ```python
     n = 3
     m = 3
     matrix1 = [[0] * m for _ in range(n)]
     
     matrix1[0][0] = 1
     
     print(matrix1)
     >>> [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
     
     matrix2 = [[0] * m] * n
     #[[0, 0, 0, 0, 0]]
     
     matrix2[0][0] = 1
     
     print(matrix2)
     >>> [[1, 0, 0], [1, 0, 0], [1, 0, 0]] # matrix2는 전체 리스트의 요소값에 영향
     ```

     matrix2의 리스트는 곰셈 연산으로 생성되었으므로 메모리 주소의 값이 같기 때문이다. (파이썬 튜터)

     리스트 컴프리헨션을 써야 원하는 인덱스의 요소를 변경할 수 있다.

## 입력 받기

1. 행렬의 크기가 미리 주어지는 경우
2. 행렬의 크기가 입력으로 주어지는 경우(크기 자체가 유동적)