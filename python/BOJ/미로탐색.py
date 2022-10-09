# 2178
import sys
sys.stdin = open("미로탐색.txt")
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# 함수 정의
def maze():
    node = deque()
    node.append((0,0))
    visited[0][0] = 1
    
    while node:
        r, c = node.popleft() 
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    node.append((nr, nc))
    
    return visited[N-1][M-1]
                    
N, M = map(int, input().split())

matrix = [list(map(int, input().rstrip())) for _ in range(N)]
# print(matrix)

visited = [[0] * M for _ in range(N)]

print(maze())






















# dr = [-1, 0, 0, 1]
# dc = [0, -1, 1, 0]

# def dfs():
#     # 시작점을 스택에 넣고 방문처리
#     stack = deque()
#     stack.append((0, 0))
#     visit[0][0] = 1
    
#     while stack:
#         # 현재 위치를 추출
#         x, y = stack.popleft()
        
#         # 델타 탐색으로 갈 수 있는 위치 탐색
#         for d in range(4):
#             nx = x + dr[d]
#             ny = y + dc[d]
            
#             # 델타 탐색 조건
#             if 0 <= nx < N and 0 <= ny < M:
#                 if matrix[nx][ny] and not visit[nx][ny]:
#                      visit[nx][ny] = visit[x][y] + 1
#                      stack.append((nx,ny))
                    
        
    
# N, M = map(int, input().split())

# matrix = [list(map(int, input().rstrip())) for _ in range(N)]
# # print(matrix)

# # 방문 리스트 생성
# visit = [[0] * M for _ in range(N)]
# # print(visit)

# dfs()
# print(*visit, sep="\n")
