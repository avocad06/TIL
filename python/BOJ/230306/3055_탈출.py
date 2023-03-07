""" 
1. 각 칸의 물이 차는 시간보다 고슴도치가 도착하는 시간이 빠르면
2. 고슴도치가 이동할 수 있는 칸
3. 각 칸마다 시작점에서부터의 최단 거리를 측정(물, 고슴도치)
"""
import sys
from collections import deque

R, C = map(int, input().split())

# 지도 입력값 받아오기
maps = [list(input()) for _ in range(R)]
# print(maps)
queue = deque()

# 물의 최단 경로
waterMap = [[-1] * C for _ in range(R)]
# 고슴도치 최단 경로
beaverMap = [[-1] * C for _ in range(R)]

# 고슴도치의 위치를 start로 정하고, 갈 수 있도록 빈 칸 '.'으로 바꾼다.
for r in range(R):
    for c in range(C):
        
        # 도착점
        cur = maps[r][c]
        if cur == 'D':
            end = (r, c)
        
        # 시작점
        elif cur == 'S':
            start = (r, c)
            beaverMap[r][c] = 0
            maps[r][c] = '.'
            
        elif cur == '*':
            queue.append((r, c))
            waterMap[r][c] = 0
            
# print(start, end)
# print(maps)

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# 각 칸당 물이 도달하는 시간을 저장한다.
while queue:
    r, c = queue.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        
        # 범위 벗어났을 경우
        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            continue
        
        # 칸이 비어있고, 방문하지 않았을 경우만,
        if maps[nr][nc] == '.' and waterMap[nr][nc] == -1:
                waterMap[nr][nc] = waterMap[r][c] + 1
                queue.append((nr, nc))
            
# print(waterMap)

# 고슴도치가 갈 수 있는 칸을 고른다.
# 고슴도치가 도달하는 시간이 물이 도달하는 시간보다 빠르다면,(작다면)
# 혹은 물이 방문할 예정이 없다면,
# 고슴도치가 이동가능한 칸
# 물과 고슴도치가 동시에 도착하면 안되므로 현재 위치 +1보다 클 때만 이동
queue.append(start)
while queue:
    r, c = queue.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        
        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            continue
        
        if maps[nr][nc] in '.D' and beaverMap[nr][nc] == -1:
            if beaverMap[r][c] + 1 < waterMap[nr][nc] or waterMap[nr][nc] == -1:
                beaverMap[nr][nc] = beaverMap[r][c] + 1
                queue.append((nr, nc))
                
# print(beaverMap)

# 고슴도치 맵의 도착 지점에 비버의 굴이 있는지 확인
D = beaverMap[end[0]][end[1]]
# 고슴도치가 비버의 굴 위치에 도달하지 못했다면,
if D == -1:
    print('KAKTUS')
# 도달했다면, 얼마나 걸렸는지 출력
else:
    print(D)