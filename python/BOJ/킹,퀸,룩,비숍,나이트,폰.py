# 3003
"""
"""
import sys
sys.stdin = open("킹퀸룩.txt")

chess = [1, 1, 2, 2, 2, 8]
piece = list(map(int, input().split()))
# print(piece)

for idx in range(len(piece)):
    print(chess[idx] - piece[idx], end = " ")