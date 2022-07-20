# 예제 03. [오류 해결] 입력 받기

# 오류코드
numbers = input().split()
# print(sum(numbers))

# 오류원인
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 정수와 문자열의 연산은 불가능합니다.

# print(sum(int(numbers)))
# 오류 원인
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# 정수 형변환 함수의 변수 타입은 문자열일 때만 가능합니다.

sum_result = []
for str in numbers : 
    sum_result += [int(str)]
    
print(sum(sum_result)) 

# map 함수를 활용하는 방법도 있을 것 같다.

