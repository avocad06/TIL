# 이차원리스트

````
< 목 차 >
1. 순회
2. 전치
3. 회전
````

## 순회

> 이중 반복문을 통해 순회

**이차원 리스트에 담긴 모든 원소를 아래와 같이 출력하고 싶다면 어떻게 할까?**

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]
>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2
```

- 행 우선 순회

  리스트를 순회하는 기존 반복문으로도 가능하다.

  **하지만, 인덱스로 접근하여 순회하는 법을 알아야 하는 이유?**

  

- 👉 열 우선 순회

  리스트를 건너뛰어가면서 순회

  단순히 m * n 으로 바뀐다고 외우지 말고, 

  한 번 <u>행렬을 좌표값(인덱스의 튜플)로 옮겨보자</u>

  **고정 값**이 무엇인지 생각해보자. (좌표(a, b)의 어느 값이 고정 값이지?)

  **다른 방식으로 순회하는 것도 있나 ?**

  

- 이차원리스트 순회 연습

  ```python
  from pprint import pprint 
  
  fa = [list(map(int, input().split())) for i in range(2)]
  sa = [list(map(int, input().split())) for i in range(2)]
  
  # new_list = [] # 비워 놓으면 안됨.
  new_list = [[0] * len(fa[0]) for i in range(2)]
  for row in range(len(fa)):
      for line in range(len(fa[0])):
          new_list[row][line] = (fa[row][line] * sa[row][line])
  
  for row in range(len(new_list)):
      for line in range(len(new_list[0])):
          print(new_list[row][line], end=" ")
      print()
  ```

  

## 전치

> 행렬의 행과 열을 서로 맞바꾸는 것을 의미한다.

열 우선 순회의 출력값은 기본적으로 행 우선 순회와 전치 행렬 관계이다.

행 우선 순회는 리스트를 순회하는 기존 반복문으로도 가능하다. 표현하는 인덱스가 같기 때문이다.

열 우선 순회는 기본적인 리스트 순회의 인덱스와 전치 행렬 관계이기 때문에,

행 우선 순회 역시 열 우선 순회와 전치 행렬의 관계가 성립한다.

행과 열의 반복횟수를 바꿔서 



## 회전
