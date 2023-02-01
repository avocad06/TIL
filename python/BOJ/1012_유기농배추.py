import sys
sys.setrecursionlimit(10 ** 6)

# 가로길이
# 세로길이
# 간선 개수
""" 
1. 입력이 들어오는 좌표를 배추(1)로 채운다
2. 배추밭을 돌면서 상,우,하,좌로 인접 배추를 확인하고
3. 범위를 벗어나지 않으면 인접 배추에 대해 dfa 수행
4. 재귀함수를 활용한 풀이라면 sys.setrecursionlimit을 써줘야 한다.
"""

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    if r <= -1 or r >= N or c >= M or c <= -1:
        # 범위를 벗어나면 바로 종료
        return False
    
    if field[r][c]:
        # 방문리스트 처리할 필요없이 바로 0으로 만들어버리기
        field[r][c] = 0
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            dfs(nr, nc)
        return True
    return False

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    # X, Y이므로 열, 행
    for _ in range(K):
        r, c = map(int, input().split())
        field[c][r] = 1
        
    # print(field)

    result = 0
    for r in range(len(field)):
        for c in range(len(field[0])):
            if field[r][c]:
                if dfs(r, c):
                    result += 1

    print(result)