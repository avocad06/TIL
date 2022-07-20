# 예제 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기

# 오류코드
# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# 오류원인
# AttributeError: 'tuple' object has no attribute 'append'
# 튜플 자료형은 리스트에 요소 값을 추가하는 .append 메소드를 사용할 수 없습니다.

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)