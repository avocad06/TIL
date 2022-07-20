import sys
sys.stdin = open('SWEA_txt/1986.txt', "r")

T = int(input())

# T만큼 테스트 케이스 실행
for test_case in range(1, T + 1):
    # N 입력받기
    N = int(input())
    # N까지 구성된 홀,짝수의 총합
    sum_result = 0
    for num in range(1, N+1):
        # 홀수면 해당 수를 빼주고, 짝수면 더해준다.
        if num % 2 != 0:
            sum_result += num
        elif num % 2 == 0:
            sum_result = sum_result - num
    print(f'#{test_case} {sum_result}', sep="")
        