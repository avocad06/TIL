# BOJ - 2669
"""
1. x, y 좌표는 100 이하인 정수로 주어진다고 했으므로 100 * 100 빈 리스트를 하나 생성
2. 값을 입력받아 색칠된 위치이면 빈 리스트의 인덱스를 1로 표시
3. 입력 받으면서 숫자 중 가장 max값을 구하고 max * max까지만 행렬을 순회
"""
import sys
sys. stdin = open("네개면적.txt")
from pprint import pprint

mr = 0
mc = 0
array = []
# 4개라 했으므로 4번을 반복
for _ in range(4):
    # 입력 값 받아오기
    numbers = list(map(int, input().split()))
    mr = max(mr, numbers[1], numbers[3])
    mc = max(mc, numbers[0], numbers[2] )
    # print(mr, mc)
    array.append(numbers)
    
mr = mr
mc = mc
board = [[0] * mc for _ in range(mr)]
# print(mr, mc)
# pprint(board)

# print(array)

# 리스트의 첫 번째 리스트는 첫 번재 사각형이다.
for arr in array:
    
    for r in range(arr[1], arr[3]):
    
        for c in range(arr[0], arr[2]):
            
            board[r][c] = 1

result = 0
for arr in board:
    result += sum(arr)

print(result)