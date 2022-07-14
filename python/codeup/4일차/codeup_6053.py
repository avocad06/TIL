#53

# 어떤 bool 값이나 변수에 not True, not False, not a 
# 와 같은 계산이 가능하다.
# 참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 
# not 예약어(reserved word, keyword)를 사용할 수 있다.
# bool 값을 다뤄주는 예약어로는 not, and, or이 있다.
# 연산결과 역시 True 또는 False의 값으로 계산된다.

b = bool(int(input()))
print(not b)

# b 는 입력값에 따라 True or False(정수 0일 경우)의 값
# 논리값을 반대로 바꿔주는 not
