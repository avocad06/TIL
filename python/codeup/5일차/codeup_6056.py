# 56

a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))
# 두 값의 True/False 값이 서로 다를 경우만 True를 출력
# not 은 bool 의 값을 반대로 해 주는 예약어
# boolean 에서 0은 False, 나머지 문자열은 True로 평가된다.