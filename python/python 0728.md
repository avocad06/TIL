## 딕셔너리(Dictionary)

````
.split() O(N)
.strip() O(N)
.find() O(N)
.count() O(N)
.replace() O(N)
````

````
< 목 차 >
1. 해시 테이블
2. 딕셔너리 기본 문법
3. 딕셔머리 메서드
````

딕셔너리의 공식 자료 구조 명칭은 '<u>해시 테이블</u>'이다.

> Non-sequence & Key-Value

쌍으로 묶여서 저장되는 데이터 타입

순회 가능하면 무조건 순서가 있지만,

순서가 있다고 무조건 순회 가능한 것은 아니다.

Key는 immutable(변경 불가능) / Value는 변경 가능



- 딕셔너리의 원리

해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수

[문자 데이터를 16진수의 고정 길이 데이터로 봐볼까(SHA256)](https://emn178.github.io/online-tools/sha256.html)

해시 : 해시 함수를 통해 얻어진 값

=> 모든 데이터를 숫자로 저장하기 때문에



- 파이썬의 딕셔너리 특징

삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다.< O(1) >

💡 Hash Function을 이용한 살술 계산으로 값이 있는 위치를 바로 알 수 있음.



- 딕셔너리 연산의 시간 복잡도

  ''딕셔너리와 리스트''의 시간 복잡도 비교

| 연산종류    | 딕셔너리                                                     | 리스트                                         |
| ----------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Get item    | 모든 operation에 O1의 시간복잡도가 걸린다(상수 복잡도를 가진다) | O(1)                                           |
| Insert item | O(1)                                                         | O(1) 또는 O(N) : 끝자리(O(1)), 중간 자리(O(N)) |
| Update item | O(1)                                                         | O(1)                                           |
| Delete item | O(1)                                                         | O(1) 또는 O(N) : 끝자리(O(1)), 중간 자리(O(N)) |
| Search item | O(1)                                                         | O(N)                                           |



- 딕셔너리는 언제 사용해야 할까?

1. 리스트를 사용하기 힘든 경우
2. 데이터에 대한 빠른 접근 탐색이 필요한 경우
3. (현실 세계의 대부분의 데이터를 다룰 경우)



### 딕셔너리 기본 문법

- 선언

  변수 = {key1:value1, key2:value2...}

```python
a = {
    "name" : "kyle",
    "gender" : "male",
    "address" : "Seoul"
}
print(a)
{'name':'kyle', 'gender':'male','address':'seoul'}
```



- 삽입/수정

  딕셔너리[key] = value

  내부에 해당 key가 없으면 삽입하고, 있으면 수정한다.

```python
john = {
    "name" : "john"
    "role" : "ceo"
}
print(john["name"])

# 왜 리스트처럼 값을 가져올 때 대괄호를 쓸까?
# 자료 구조의 차이(리스트라서 대괄호를 쓰는게 아니고, 딕셔너리라서 중괄호를 쓰는게 아니듯이)보다는 조회 구문에 대괄호([])를 사용하기 때문에 값을 가져올 때 대괄호를 쓴다.
```



```python
# counting

scores = ["A,", "A", "B", "C", "D", "A", "B"]

a = 0
b = 0
c = 0
d = 0

for score in scores:
    if score == "A":
        a+=1
    else:
        
        
counter = {
    "a" : 0,
    "B" : 0,
    "C" : 0,
    "D" : 0
}
for score in scores:
    counter[score] += 1
    
print(counter)
```

- 삭제

  내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 KeyEroor 발생

  딕셔너리.pop(key) : return값이 있다. 삭제보다는 빼낸다는 의미로 보면 좋다.

  딕셔너리.pop(key, default) 두 버너재 인자로 기본값을 지정하여 KeyError 방지 가능



- 조회

  key에 해당하는 value 반환

  딕셔너리[key]

  딕셔너리.get(key)



- 딕셔너리 기본 문법 정리



### 딕셔너리 메서드

```python
.keys()
.values()
.items()
```

딕셔너리는 non sequence지만 iterable하게 만들 수는 있다.

반복문 사용하기

딕셔너리 순회는 **키를 순회**, value순회를 위해서는?

[대괄호]

1. .keys()

   딕셔너리

   어떨 때 쓰나요 ? 키가 몇 개 있나요? ex) len

2. .values()

3. .items()

   ```python
   # key, value를 같이 순회하는
   for key, value in john.items()
   # for (key, value) in john.items()
   # for (k, v) in john. items()
   ```

- 딕셔너리 활용 연습
- 코드리뷰할 때 문제를 어디를 어떻게 쪼갰는지