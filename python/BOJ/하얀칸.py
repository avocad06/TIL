# 1100
"""
"""
import sys
sys.stdin = open("하얀칸.txt")

matrix = [input() for _ in range(8)]
# print(matrix)
cnt = 0
for r in range(8):
    if r % 2 == 0:
        for c in range(0, 8, 2):
            if matrix[r][c] == 'F':
                cnt += 1
    
    elif r % 2 == 1:
        for c in range(1, 8, 2):
            if matrix[r][c] == 'F':
                cnt += 1

print(cnt)