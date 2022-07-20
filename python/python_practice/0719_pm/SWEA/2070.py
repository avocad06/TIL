import sys
sys.stdin = open('2070.txt','r')

T = int(input())

for i in range(1, T+1):
    a, b = map(int,input().split())
    a, b <= 10000
    if a > b:
        print(f'#{i} >', sep=" ")
    elif a < b:
        print(f'#{i} <', sep=" ")
    else :
        print(f'#{i} =', sep=" ")
    