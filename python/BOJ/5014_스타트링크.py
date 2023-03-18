# 5014
""" 
1. 각 층에 도달하는 최단 거리를 저장한다.
2. S층은 1번 만에 도달할 수 있다.
3. 인접노드는 각각이기 때문에, 범위를 같이 생각하면 안 된다.(nu, nd)
4. 범위 체크는 방문할 수 있는 층수여야 한다.(0층 안 됨)
"""
from collections import deque

F, S, G, U, D = map(int, input().split())
visitList = [0] * (F + 1)

answer = "use the stairs"

def bfs(S):
    queue = deque()
    queue.append(S)
    if S == G:
        print(0)
        return True
    visitList[S] = 1
    
    while queue:
        node = queue.popleft()
        
        if node == G:
            print(visitList[node] - 1)
            return True
        
        for x in [-D, U]:
            nx = node + x
            if nx < 1 or nx >= F + 1:
                continue
            
            if not visitList[nx]:
                visitList[nx] = visitList[node] + 1
                queue.append((nx))

if not (bfs(S)):
    print(answer)