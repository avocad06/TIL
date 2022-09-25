# 2001
"""
"""
import sys
sys.stdin = open("파리퇴치.txt")

""" 
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
"""
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # N ,M = 5, 2

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(matrix)
    # matrix = [[1, 3, 3, 6, 7], 
    #           [8, 13, 9, 12, 8], 
    #           [4, 16, 11, 12, 6], 
    #           [2, 4, 1, 23, 2], 
    #           [9, 13, 4, 7, 3]]

    # print(flys)
    mx = 0
    for c in range(len(matrix[0])):
        
        for r in range(len(matrix)):
            
            # 각 슬라이싱의 합을담을 변수
            small = 0
            if r + M - 1 <= len(matrix) - 1 and c + M -1 <= len(matrix[0]) -1:
                for idx in range(M):
                    small += sum(matrix[r + idx][c:c+M])
                
                mx = max(mx, small)         
    print(f'#{t} {mx}')