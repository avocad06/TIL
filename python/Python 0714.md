변수에 저장, 조건/반복문에 따라서 조작(계산)한다.

타입(int float complex bool str list tuple range set dictionary)

내장함수는 input의 type을 잘 생각해야 한다.

output의 type은 또 어떻지 ?

**데이터타입.메서드()**

타입(s)을 -v

1. 누가 할 수 있는가?(타입)
2. 메서드(input)에 무엇을 넣는가?
3. output은 어떻게 되는가?

# 시퀀스 메서드(순서가 있는)

> 문자열, 리스트

## 문자열 

- s.find
- 

## 리스트

mutable(변경 가능하다)

- 값 추가
  - .append 맨 뒤에 추가
  - .insert 원하는 위치(인덱스)에 추가

- 값 삭제
  - .remove
  - .pop 정해진 위치에 있는 값을 삭제하고 삭제한 값을 반환
  - .clear 리스트 항목들 모두 삭제

 - 탐색 및 정렬
   - .index 위치를 찾아서 반환
   - .count 원하는 값의 개수를 반환
   - .sort 

## 딕셔너리

- .get key를 통해 value를 가져옴
  - 원래라면 key error가 발생하지만 <u>.get을 쓰면 none이라는 값을 반환함.</u>

- .pop default값이 없으면 key eroor