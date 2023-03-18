# 5014
from collections import deque

F, S, G, U, D = map(int, input().split())
visitList = [0] * (F + 1)

answer = "use the stairs"

def bfs(v):
    queue = deque()
    queue.append((S, v))
    
    while queue:
        node, cnt = queue.popleft()
        # visitList[node] = node
        print(node, cnt)
        
        if node == G:
            print(cnt)
        
        nu = node + U
        nd = node - D
        
        if nu < 0 or nu >= F or nd < 0 or nd >= F:
            continue
        
        if not visitList[nu]:
            visitList[nu] = visitList[node] + 1
            queue.append((nu, visitList[node] + 1))
        if not visitList[nd]:
            visitList[nd] = visitList[node] + 1
            queue.append((nd, visitList[node] + 1))

if not (bfs(1)):
    print(answer)