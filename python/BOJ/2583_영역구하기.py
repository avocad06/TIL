# 2583
""" 
1. 너비를 구하는 것이므로 모눈종이의 너비만 보장되면 y의 값은 상관이 없다.
"""
from pprint import pprint
from collections import deque
M, N, K = map(int, input().split())

board = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    
    for r in range(y1, y2):
        for c in range(x1, x2):
            board[r][c] = 1

# pprint(board)

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def bfs(start):
    queue = deque()
    queue.append((start))
    # 각 영역의 넓이를 카운트할 변수
    cnt = 1
    
    while queue:
        r, c = queue.popleft()
        board[r][c] = 1
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr < 0 or nr >= M or nc < 0 or nc >= N:
                continue
            
            if board[nr][nc]:
                continue
            
            if not board[nr][nc]:
                board[nr][nc] = 1
                queue.append((nr, nc))
                # 영역이 늘어날 때마다 카운트
                cnt += 1
    return cnt

answer = []
result = 0
for r in range(M):
    for c in range(N):
        if not board[r][c]:
            answer.append(bfs((r, c)))

print(len(answer))            
print(*sorted(answer))