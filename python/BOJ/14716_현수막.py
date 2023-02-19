""" 
1. 1이 상,하,좌,우, 대각선으로 인접 서로 연결 = 한 개의 글자로 생각
2. 그랬을 때 글자의 개수는?
"""
from collections import deque

M, N = map(int, input().split())

words = [list(map(int, input().split())) for _ in range(M)]
# print(words)

# 8방 탐색
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    
    while queue:
        r, c = queue.popleft()
        
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 > nr or nr > M or nc < 0 or nc > N:
                continue
            
            if words[nr][nc]:
                words[nr][nc] = 0
                queue.append((nr, nc))
    
    return True

result = 0
for r in range(M):
    for c in range(N):
        if words[r][c] and bfs(r, c):
            result += 1
            
print(result)