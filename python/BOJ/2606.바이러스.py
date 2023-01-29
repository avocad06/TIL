import sys
input = sys.stdin.readline

"""
1. 연결되어 있지 않은 컴퓨터는 바이러스의 영향을 받지 않는다.
2. 컴퓨터의 수는 노드의 수(1부터 100 이하까지)
3. 컴퓨터 쌍의 수 = 간선 개수
3. 둘째 줄 이상부터 => 노드 간의 관계 => 인접리스트를 만들어서 풀어야할 거 같다.
4. 1번 컴퓨터를 통해 웜 바이러스에게 걸리게 되는 컴퓨터의 수 출력하기
"""
# 노드의 수
N = int(input())
# 간선 수
M = int(input())


result = 0
def dfs(v, result):
    visited[v] = 1
    
    for i in link[v]:
        if not visited[i]:
            # dfs의 반환값이 result 이기 때문에
            result = dfs(i, result)
            result += 1
    return result
    

# 인접리스트        
link = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
    
# 방문리스트
visited = [0] * (N + 1)

print(dfs(1, result))



