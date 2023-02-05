""" 
1. 1행 1열로 시작한다.(시작점은 0, 0)
# 세로 R칸, 가로 C칸이다.
2. 상하좌우로 인접한 네 칸 중 한 칸으로 이동이 가능하다.
3. 지금까지 지나온 칸에 적혀있는 알파벳과는 달라야 한다.
4. 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
5. 좌측 상단에서 시작한 말이 최대한 몇 칸을 지날 수 있는지 구하기
6. 좌측 상단의 칸도 포함한다.

방문한 알파벳을 언제 저장해 놔야 할까?
[전역 변수로 하고, dfs가 끝나면 초기화]
==================================================================
global => 함수 안에서 전역변수를 만드는 방법
answer는 전역으로 값이 일정해야하므로 


"""

import sys

R, C = map(int, input().split())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c, count):
    # 글로벌 변수 선언
    global answer
    # 알파벳 방문했는지
    global visited
    # 현재 최대 칸과 비교
    answer = max(answer, count)
    
    # 델타 탐색
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        
        # nr, nc의 범위 벗어나지 않을 때
        # 아직 방문하지 않은 알파벳이라면
        if 0 <= nr < R and 0 <= nc < C and not visited[matrix[nr][nc]]:
            # 방문처리하고,
            visited[matrix[nr][nc]] = True
            # nr, nc에 대해 dfs 진행
            dfs(nr, nc, count + 1)
            # dfs가 끝나면 알파벳 리스트는 초기화
            visited[matrix[nr][nc]] = False
    
# 입력값 : 입력값을 숫자로 바꿔주는 익명함수를 map으로 모든 문자에 적용한 리스트라는 의미
matrix = [list(map(lambda i: ord(i) - 65, input())) for _ in range(R)]

answer = 1
visited = [False] * 26
# 시작점은 True
visited[matrix[0][0]] = True
dfs(0, 0, 1)

print(answer)