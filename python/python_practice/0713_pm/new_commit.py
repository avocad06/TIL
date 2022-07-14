#13. 주어진 word를 역순으로 출력해보세요.
 
word = 'apple'

# 1. for문
result = ''
#result 값 초기화. 현재 result값에는 빈 문자열이 있다.
#for i in word:
    # result = i + result
    # result의 type은 str. str끼리의 연산 가능. 
    # i 에 대입된 word의 요소에 result를 합하는 식이라면?
    #해당 식을 for 없이 실행하면(type확인)
# result = word[0] + result
# print(result, type(result)) a <class 'str'>
# result = word[1] + result
# print(result, type(result)) pa <class 'str'>
# result = word[2] + result
# print(result, type(result)) ppa <class 'str'>
# result = word[3] + result
# print(result, type(result)) lppa <class 'str'>
# result = word[4] + result
# print(result, type(result)) elppa <class 'str'>
    #반복해야 하는 것은 문자열 전부를 순회, 순회할 때마다 result 값을 추가
for i in word:
    result = i + result
print(result)

# 2. pythonic(문자열을 역순으로 슬라이싱)
word = 'apple'

# range 연습(역순 출력하기)
# print(list(range(6,0,-3)))
print(word[::-1])
# 처음부터 끝까지 슬라이싱하는데 -1씩 이동하면서 출력

# 3. index
word = 'apple'

# range 범위에 있는 숫자를 꺼내와서 인덱스의 순서에 집어넣고 
# 원하는 인덱스의 값을 출력하는 것을 반복할 것입니다.
# 어떤 숫자를 꺼내올 건가요?

for i in range(len(word)):
# apple 글자 수 미만까지 만들어진 숫자를 꺼내와서, 그 범위만큼 반복하겠습니다.
    print(word[i])
# range의 숫자를 꺼내서 접근하고자 하는 인덱스의 순서에 집어넣고 출력하는 것을 반복할 것입니다.
print(list(range(len(word))))
# len(word)=5 이므로 range의 범위는 5미만의 리스트 [0, 1, 2, 3, 4]입니다.
# 즉, 반복문에는 word[0], word[1],,,word[4]가 입력되고, 해당 인덱스는 apple그대로를 출력합니다.
# 원하는 인덱스의 값에 접근하도록 출력 함수를 조정해보자.
# 우리가 원하는 인덱스(역순)는 word[4], word[3],,,,word[0] 순으로 출력 되는 것
# [0]이 [4]가 되고, [4]가 [0]이 되려면 word[4-0], word[4-1],,,word[4-4]의 형태가 되면 된다.