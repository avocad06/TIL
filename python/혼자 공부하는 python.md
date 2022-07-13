혼자 공부하는 python

## 실습 9번) 이영희의 총 득표 수는?

```python
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
n = 0 # students 리스트 요소를 대입하다가 '이영희'와 만난 통

for i in students:
    if i == '이영희': # '이영희'와 만났을 때
        n += 1 # 통 안의 수는 증가(안 만났으면 증가 안 하는거고,)
print(n) # 그래서 총 몇 개의 '이영희'가 나왔니?
```



## 실습 10번) 5의 개수는?

```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

numbers_count = 0 # numbers에서 원하는 수 갯수 카운팅했다

for num in numbers :
    # numbers 리스트에 있는 요소들, 즉 num에 대입되는 애들은 type이 str인가요? int인가요?
	# print(type(num)) 해 보면 됩니다.
    # int
    if num == 5 : # 리스트 요소들(num)이 5를 만났을 때
        numbers_count = numbers_count+1 # 카운팅 갯수가 증가해요
print(numbers_count) # 그래서 총 몇 개가 카운팅 되었니?
```



## 실습 11번)  구구단 출력하기

```python
# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

for x in range(2,10): # range의 범위를 모두 반복해서 x 에 넣어주세요
    for y in range(1,10): # range의 범위를 모두 반복해서 y 에 넣어주세요(단, x의 실행에 y 실행도 포함되어야 해요 그러므로 x에 대한 for문 안에 y에 대한 for문이 들어가는 것)
        print(f`{x}x{y}={x*y}`) #f-string을 이용해서 값을 문자열로 변환해주세요.
```



## 실습 12번) a를 모두 제거해보자

```python
#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
word = 'apple'
answer = '' # a가 아닌 문자들을 모을 통을 만들게요. 근데 이제 문자열인.
for i in word : # word의 값을 모두 순회해서 i에 대입해주세요
    if i != 'a' : # i(word 중에서 대입된 값)가 a랑 같지 "않으면(!=)"
        answer += i # a가 아닌 문자들을 모아놓은 통에 i를 추가할게요. 문자열도 추가를 할 수가 있어요. (문자열의 연산)
print(answer) 
```



## 실습 13번) apple을 역순으로 적어보자

```python
#주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
word = 'apple'
word_count = 0 # word의 글자 수를 세서 저장할 통
for num in word: # word의 요소를 하나 순회해서 num에 대입할 거예요
    word_count += 1 # num에 대입을 할 때마다(순회를 하나씩 할 때마다) 글자 수를 하나씩 증가시킬 거예요.
for i in range(word_count-1,-1,-1): # 맨뒤 자리부터 0의 자리까지 -1씩 진행하면서 순회할 거예요.
    print(word[i], end="") # 인덱스로 접근 해서 i에 대입된 숫자에 맞는 인덱스의 위치에 있는 i 값을 출력할 거예요.
    # word[4], word[3], word[2], word[1] 로 해서 end="" 로 출력이 완료된 내용을 수정해줄 거예요.
```

