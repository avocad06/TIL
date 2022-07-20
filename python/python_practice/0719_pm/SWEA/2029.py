import sys
sys.stdin = open('2029.txt','r')

T = int(input())

for i in range(1,T+1):
    a, b = list(map(int,input().split()))
    print(f'#{i} {a//b} {a%b}' ,sep=" ")
