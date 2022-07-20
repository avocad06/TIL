# 예제 05. [오류 해결] 숫자의 길이 구하기

# 오류코드
number = 22020718
# print(len(number))

# 오류원인
# TypeError: object of type 'int' has no len()
# 정수는 함수 len으로 길이를 구할 수 없습니다.

number = str(number)
print(len(number))