""" 
1. 두 개의 bfs를 진행한다.
2. bfs가 한 번 종료되면 섬 한 개를 다 돈 것
3. 각각의 섬별로 다른 섬까지의 최소 거리를 측정한 거리 저장 배열을 만든다.
4. 전역변수를 활용
"""
from collections import deque
from pprint import pprint as print
import sys


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
# 섬의 개수이기도 함
cnt = 1
for r in range(N):
    for c in range(N):
        if maps[r][c] == 1:
            # 땅을 찾았다면 시작 지점부터 번호 매기기
            maps[r][c] = cnt + 1
            bfs_1(r, c, cnt + 1)
            cnt += 1

print(maps)

# 가장 짧은 공백 세기
def bfs_2(start):
    
    global result
    queue = deque()

    # 각 섬에 대응하는 checkList 생성
    checkList = [[-1] * N for _ in range(N)]
    
    # 섬에 해당하는 영역의 번호를 0으로 초기화
    for r in range(N):
        for c in range(N):
                # start와 같은 섬이라면,
                if maps[r][c] == start:
                    queue.append((r, c))
                    # 0으로 초기화
                    checkList[r][c] = 0
    
    while queue:
        r, c = queue.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            
            # 섬은 섬인데 start와 다른 섬이라면,(다른 섬을 만났음)
            if maps[nr][nc] and maps[nr][nc] != start:
                # print(start)
                # print(checkList)
                result = min(result, checkList[r][c])
                return
            
            # 바다라면
            # 바다이고, 방문하지 않았다면,
            if not maps[nr][nc] and checkList[nr][nc] < 0:
                # 이전 거리값 + 1
                checkList[nr][nc] = checkList[r][c] + 1
                queue.append((nr, nc))
                
result = sys.maxsize

for num in range(1, cnt):
    bfs_2(num + 1)
    
print(result)