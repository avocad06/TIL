# 1453
import sys
sys.stdin = open("피시방알바.txt")

int(input())
call = list(map(int, input().split()))
result = set(call)
print(len(call) - len(result))
