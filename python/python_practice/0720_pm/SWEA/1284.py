import sys
sys.stdin = open('SWEA_txt/1284.txt', "r")

# A사 : 1L * P원 W*P
# B사 :
# R 이하 : Q
# R 초과 : Q + S*(W-R)


T = int(input())
for test_case in range(1, T+1):
    P, Q, R, S, W = map(int,input().split())
    # 5 개도 map split이 되는구나
    tax_A = W*P
    # W는 한 달 사용량
    tax_B = Q if W < R else Q + (W-R) * S
    # 최소값 찾기
    print(f'#{test_case} {min(tax_A, tax_B)}', sep=" ")