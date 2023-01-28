import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v):
    # 들어온 노드를 방문처리하고
    visited[v] = 1
    # 인접 리스트를 순회해서
    for i in link[v]:
        # i번째 노드가 방문처리되지 않았으면
        if not visited[i]:
            # 다시 dfs
            dfs(i)
            
n, m = map(int, input().split())
visited = [0 for _ in range(n + 1)]
# 인접리스트
link = [[] for _ in range(n + 1)]
# 연결 요소의 개수
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

for i in range(1, n + 1): # 1번 노드부터 돌면서
    if not visited[i]:
        dfs(i)
        result += 1

print(result)
