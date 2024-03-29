# 6081.
"""
A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)

# 입력
16진수로 한 자리 수가 입력된다.
단, A ~ F 까지만 입력된다.

# 출력
입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다.
계산 결과도 16진수로 출력해야 한다.

"""
n = int(input(), 16)
for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep="")
