""" 
1. 상, 하, 좌, 우로 dfs를 해봐야 한다.
2. 범위를 벗어나면 즉시 종료해야 한다.
3. global cnt
4. 방문리스트를 굳이 쓸 필요는 없다(방문한 좌표를 0으로 만들어주면 되니까)
"""
from pprint import pprint
import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

town = []
for _ in range(N):
    town.append(list(map(int, input())))
    
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    if r <= -1 or r >= N or c <= -1 or c >= N:
        return False # 범위를 벗어나면 즉시 종료
    
    # 집인데 방문하지 않았으면
    if town[r][c]:
        # print(r, c, v)
        global cnt
        cnt += 1
        # 방문 처리
        town[r][c] = 0
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            dfs(nr, nc)
        return True
    
    return False

cnt = 0
result = 0
answer = []

# 모든 town 순회
for r in range(N):
    for c in range(N):
        # 1부터 시작
        if town[r][c]:
            # True이면 단지 하나를 다 돌았다는 뜻
            if dfs(r, c):
                answer.append(cnt)
                result += 1
                # 단지 하나를 다 셀 때마다 count 초기화
                cnt = 0
                
answer = sorted(answer)
print(result)
print(*answer, sep='\n')