# 1236
"""
"""
import sys
sys.stdin = open("성지키기.txt")

N, M = map(int, input().split())

castle = [input() for _ in range(N)]
# print(castle)

# 추가 경비원이 필요한 행의 수를 저장
add_row = 0
# 추가 경비원이 필요한 열의 개수를 저장하는 리스트
add_col = [0] * M
# print(add_row, add_col)

for r in range(len(castle)):
    if 'X' not in castle[r]:
        add_row += 1
        
    for c in range(len(castle[0])):

        var = castle[r][c]
        # print(var)
        if var == 'X':
            add_col[c] += 1          

if add_row == 0:
    print(add_col.count(0))
else:
    print(add_row)
