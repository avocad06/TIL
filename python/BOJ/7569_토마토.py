import sys
from collections import deque

m, n, h = map(int, input().split())

matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

queue = deque()

dr = [-1,1,0,0,0,0]
dc = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]

answer = 0

def bfs():
    while queue:
        r,c,h = queue.popleft()

        for d in range(6):
            nr = r + dr[d]
            nc = c + dc[d]
            nh = h + dh[d]

            if nr < 0 or nr >= h or nc < 0 or nc >= n or nh < 0 or nh >= m:
                continue

            if matrix[nr][nc][nh] == 0 and visited[nr][nc][nh] == False:
                queue.append((nr,nc,nh))
                matrix[nr][nc][nh] = matrix[nr][nc][nh] + 1
                visited[nr][nc][nh] = True


# 모두 1이 아닐 경우

for a in range(h):
    for b in range(n):
        for c in range(m):
            if matrix[a][b][c] == 1 and visited[a][b][c] == 0:
                queue.append((a,b,c))
                visited[a][b][c] = True
bfs()

# 토마토 확인

for a in matrix:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)            
        answer = max(answer, max(b))

print(answer-1)