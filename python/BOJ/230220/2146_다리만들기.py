""" 
1. 
"""
from collections import deque
from pprint import pprint


N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]
# print(maps)

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def bfs_1(r, c, start):
    queue = deque()
    queue.append((r, c))
    
    while queue:
        r, c = queue.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 > nr or nr >= N or 0 > nc or nc >= N:
                continue
            
            if maps[nr][nc] == 1:
                # 섬별 번호 붙이기
                maps[nr][nc] = start
                queue.append((nr, nc))

# 번호 붙이기
cnt = 1
for r in range(N):
    for c in range(N):
        if maps[r][c] == 1:
            bfs_1(r, c, cnt + 1)
            cnt += 1

checkList = [[-1] * N for _ in range(N)]
# 가장 짧은 공백 세기
# print(checkList)

def bfs_2(r, c, start):
    queue = deque()
    queue.append((r, c))
    checkList[r][c] = 0
    
    while queue:
        r, c = queue.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            
            # 섬이라면
            if maps[nr][nc]:
                # start와 같은 섬이라면,
                if maps[nr][nc] == start:
                    # 0으로 초기화
                    checkList[nr][nc] = 0
                    continue
                
                # start와 다른 섬이라면,(다른 섬을 만났음)
                else:
                    # 섬으로 만들고
                    checkList[nr][nc] = 0
            
            # 바다라면
            # 바다이고, 방문하지 않았다면,
            if not maps[nr][nc] and checkList[nr][nc] < 0:
                # 이전 거리값 + 1
                checkList[nr][nc] = checkList[r][c] + 1
                queue.append((nr, nc))
                
result = N ** 2
for r in range(N):
    for c in range(N):
        if maps[r][c]:
            tmp = bfs_2(r, c, maps[r][c])
            if tmp:
                print(tmp)
                min(result, tmp)

pprint(checkList)

