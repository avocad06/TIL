import sys
sys.stdin = open('1284.txt', "r")

# A사 : 1L * P원 W*P
# B사 :
# R 이하 : Q
# R 초과 : Q + S*(W-R)


T = int(input())
for test_case in range(1, T+1):
    P, Q, R, S, W = map(int,input().split())
    # 5 개도 map split이 되는구나
    W <= 10000
    tax_A = W*P
    # W는 한 달 사용량
    tax_B = Q
    if W > R:
        tax_B = Q + (W-R)*S
    print(f'#{test_case} {tax_A if tax_A < tax_B else tax_B}', sep=" ")