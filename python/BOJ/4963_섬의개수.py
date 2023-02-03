"""
1. 가로, 세로 또는 대각선 = 같은 섬
2. land는 1 => 1로 된 칸만 갈 수 있음.
"""

import sys
sys.setrecursionlimit(10 ** 6)

# 8방향
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(r, c):
    if r < 0 or r >= h or c < 0 or c >= w:
        return False
    
    if matrix[r][c] and not visited[r][c]:
        visited[r][c] = 1

        # print(visited)
        
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            
            dfs(nr, nc)
        return True
    
    return False

while True:
    w, h = map(int, input().split())
    
    if not (w + h):
        break
    
    visited = [[False] * w for _ in range(h)]
    
    matrix = [list(map(int, input().split())) for _ in range(h)]
    
    answer = 0
    for r in range(h):
        for c in range(w):
            # 땅이고 아직 방문 안 한 칸이면 dfs 수행
            if matrix[r][c] and not visited[r][c]:
                if dfs(r, c):
                    answer += 1
    print(answer)