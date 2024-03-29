# 코드리뷰

- 파리퇴치

````
범위 정하기
N - M 부터 출력을 해봐서 필요한 값의 범위가 어디인지 찾기
````

- 어디에 단어가 들어갈 수 있을까

  

# 이차원리스트 - 회전

문제에서 이차원 리스트를 **왼쪽, 오른쪽으로 90도 회전**하는 경우가 존재한다.

✔ 원데이터와 90도로 바뀐 데이터를 보고, [0] * n 의 새로운 리스트를 만들어서 인덱스를 확인해보기 <u>외우지말고 일반항을 뽑아가는 과정을 기억하기</u>

180도는 90도 회전 for 문을 2번 반복, 270도는 3번 반복



# 완전탐색 I (Exhaustibe Search)

````
< 목 차 >
1. 무식하게 풀기(Brute-force)
2. 델타 탐색(Delta Search)
````



## Brute-force

> **모든 경우의 수를 탐색**하여 문제를 해결하는 방식

- 가장 단순한 풀이 기법, 단순 조건문과 반복문을 이용해서 풀 수 있다.
- 복잡한 알고리즘보다는, <u>**아이디어를 어떻게 ''코드''로 구현할 것인지**</u>가 중요
- 시간복잡도 측면에서 효율성은 떨어질 수 있음.
- 문제 풀이의 기초

- BOJ 2798. 블랙잭

  모든 조합을 다 뽑아서 다 더해 보기

- 모든 문제를 접근할 때 처음에는 브루트포스로 접근하는 게 좋다.

  코드 말고, 생각을 해보자

  

## 델타 탐색 (Delta Search)

> 각 지점에서 **상하좌우에 위치한 다른 지점을 조회하거나 이동**하는 방식

- 이차원 리스트의 완전탐색에서 많이 등장하는 유형

- 델타탐색(상하좌우 탐색)

- 단순히 요소가 아니라 인접한 원소의 차이값(델타)

- 리스트의 인덱스(좌표)의 조작

- 행과열의 변량 = `델타(delta)`

- 델타 리스트를 만들어도 되지만(ex) (`dx`, ` dy`)

- only 파이썬에서는 <u>좌표값 자체를 리스트</u>에 넣어도 된다. ( 튜플 덧셈 )

  ````python
  delta = [(-1, 0), (1, 0), (0, -1), (1, 1)] # 좌표값이 리스트 안에
  
  # 지점 좌표 (1, 1)
  # 4방위 탐색
  for i in range(4):
      for j in range(4):
          # i, j = 0, 0 ~ 3, 3
          # i, j = 1, 1
          for d in delta:
              print(i + d[0], j + d[1]) # 튜플의 요소를 순회
  ````

  ```python
  # 튜플로 델타 리스트 뽑아내기
  dr = []
  dc = []
  d_list = [(0, -1), (-1, 0), (1, 1), (1, 0)]
  for idx in range(len(d_list)):
      dr.append(d_list[idx][0]) # 튜플의 요소를 순회
      dc.append(d_list[idx][1])
  print(dr, dc)
  >>> dr = [0, -1, 1, 1]
  >>> dc = [-1, 0, 1, 0]
           # 좌 상 우 하
  ```

  ✔ 움직일 때마다 변화량을 뽑아낼 수 있는 코드를 만들어낼 수 있어야 한다.

  

### 델타 탐색의 예외처리(범위 갱신)

  ```python
  if 0 <= dr_r < 3 and 0 <= dc_c < 3: # dr_r, dc_c 는 0, 1, 2
      r = dr_r
      c = dc_c
  ```

- 델타탐색 정리

  ````
  1. 델타설정
  2. 델타 순회
  3. 경계값을 정리
  ````

  ```python
  N, M = 3, 5
  
  # 1. 델타값 정의(좌상우하)
  dr = [0, -1, 1, 1]
  dc = [-1, 0, 1, 0]
  
  # 2. 이차원 리스트 순회
  for r in range(N):
      for c in range(M):
          
          #3. 델타값을 이용해 상하좌우 이동
          for d in range(4):
              dr_r = r + dr[d]
              dc_c = c + dc[d]
              
              # 4. 범위를 벗어나지 않으면 갱신
              if 0 <= dr_r <= 3 and 0 <= dc_c <= 3:
                  r = dr_r
                  c = dc_c
  ```

  
