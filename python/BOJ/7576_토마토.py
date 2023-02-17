from collections import deque

M, N = map(int, input().split())
# N, M, H = 5, 3, 2

# 위 = r - M, 아래 = r + M
dr = [-1, 0, 0, 1]
dc= [0, -1, 1, 0]

# 입력값받기
tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque()                   
for r in range(N):
    for c in range(M):
            
        if tomato[r][c] == 1:
            queue.append((r, c))
            
def bfs():
    while queue:
        r, c = queue.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            if not tomato[nr][nc]:
                tomato[nr][nc] = tomato[r][c] + 1
                queue.append((nr, nc))
        
bfs()

result = 0
for r in range(N):
    for c in range(M):
        # 어차피 max값이 1이고, 1로만 구성돼있으면
        # 토마토가 없는 칸이면 -1 -1 = -2, result 초기값이라서 0
        result = max(result, tomato[r][c] - 1)
        
        if not tomato[r][c]:
    
            result = -1
            break
    
    if result < 0:
        break
      
print(result)