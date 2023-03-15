from collections import deque

n, m = map(int, input().split())

paint = [list(map(int, input().split())) for _ in range(n)]

# print(paint)

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def bfs(start):
    queue = deque()
    queue.append(start)
    cnt = 1
    
    while queue:
        r, c = queue.popleft()
        paint[r][c] = 0
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            
            if not paint[nr][nc]:
                continue
            
            paint[nr][nc] = 0
            cnt += 1
            queue.append((nr, nc))
    
    return cnt

maxWidth = 0
result = 0

for r in range(n):
    for c in range(m):
        if paint[r][c]:
            maxWidth = max(maxWidth, bfs((r,c)))
            result += 1
            
print(result, maxWidth, sep="\n")