# 1743
from collections import deque

N, M, K = map(int, input().split())

cor = [["."] * M for _ in range(N)]

# print(cor)

for _ in range(K):
    r, c = map(int, input().split())
    cor[r - 1][c - 1] = '#'
    
# print(cor)

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def bfs(start):
    queue = deque()
    queue.append(start)
    cnt = 1
    
    while queue:
        r, c = queue.popleft()
        cor[r][c] = 0
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            if not cor[nr][nc]:
                continue
            
            if cor[nr][nc] == '#':
                cor[nr][nc] = 0
                cnt += 1
                queue.append((nr, nc))
            
    return cnt

maxNum = 0
for r in range(N):
    for c in range(M):
        if cor[r][c] == '#':
            maxNum = max(maxNum, bfs((r, c)))

print(maxNum)