""" 
1. 색약인 경우 G을 R로 바꿔주는 작업은 따로 해야한다.
"""


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r, c):
    #현재 색상 좌표를 방문해준다.
    visited[r][c] = True
    current_color = matrix[r][c]

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0 <= nr < n) and (0 <= nc < n):
            #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visited[nr][nc]==False:
                if matrix[nr][nc] == current_color:
                    dfs(nr,nc)

for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if visited[i][j]==False:
            dfs(i,j)
            three_cnt += 1

#R을 G로 바꾸어준다. --> 적록색약은 같은 색으로 보기 때문에
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='R':
            matrix[i][j]='G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)