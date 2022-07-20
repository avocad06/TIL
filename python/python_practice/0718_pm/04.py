# 예제 04. [오류 해결] 입력 받기 - 2

# 오류코드
# words = list(map(int, input().split()))
# print(words)

# 오류원인
# ValueError: invalid literal for int() with base 10: "I'm"
# 정수형의 문자열이 아닌 문자열은 int 함수로 형 변환할 수 없습니다.

words = list(map(str, input().split()))
print(words)