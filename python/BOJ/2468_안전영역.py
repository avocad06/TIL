""" 
1. 지점의 높이 정보가 주어질 때, 물에 잠기지 않는 안전한 영역의 최대 개수를 계산
2. 테스트케이스의 개수는 주어지는 수 중 가장 높은 수만큼
3. 아무 지역도 물에 안 잠길 때 안전 영역은 1개(다 이어져있을 거라서)
4. N은 100까지 
5. 높이는 1이상이므로 방문한 노드이면 0으로 바꾸기(경우의 수가 증가할 때마다 초기화시키기)
6. 반례 없었으면 틀렸을 문제

방문리스트를 만들어서 풀었는데 다른 풀이방법은 없나?
=> 최고 높이까지 오면 모두 잠기니까 최고 높이 -1까지만 계산한다.(최고 높이가 9라면 0부터 8까지 돌고 안전한 영역 개수 구해도 된다.)
=> nr, nc에 대한 유효성을 먼저 판단하면 재귀의 깊이가 매우매우 많이 줄어든다.(그런가?)

"""
import sys
sys.setrecursionlimit(10 ** 6)

# 입력값받기
N = int(input())

# 최대로 살펴봐야할 경우의 수
M = 0
# 아무 지역도 물에 안 잠기는 경우 => 안전영역은 1개
answer = 1
matrix = []
for _ in range(N):
    arr = list(map(int, input().split()))
    M = max(M, max(arr))
    matrix.append(arr)

# print(M)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, cnt):
    if r >= N or r < 0 or c >= N or c < 0:
        return False
    
    if not visited[r][c]:
        visited[r][c] = 1
        # print(matrix)
        
        if matrix[r][c] > cnt:
            
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                dfs(nr, nc, cnt)
            return True
    return False

for cnt in range(1, M + 1):
    visited = [[False] * N for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if dfs(r, c, cnt):
                    result += 1
                    
    answer = max(result, answer)

print(answer)
