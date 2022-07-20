
N = int(input())

# 1부터 N 까지 순회
for divisor in range(1, N+1):
    # N 의 나머지가 0인 경우만 출력
    if N % divisor == 0:
        print(divisor, end=" ")