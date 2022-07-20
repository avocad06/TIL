import sys
sys.stdin = open('2071.txt','r')

T = int(input())

for i in range(1, T+1):
    number = list(map(int,input().split()))
    avg = round(sum(number)/len(number))
    print(f'#{i} {avg}',sep=" ")