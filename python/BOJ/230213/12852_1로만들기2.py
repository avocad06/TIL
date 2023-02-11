""" 
1. 연산 횟수의 최솟값 => 최단 거리
2. 방문했던 노드를 어떻게 처리하지?
=> 방문 리스트 만들면 되지
3. ==============================
- 메모제이션으로 1부터 1억까지 각 숫자에서 발생할 수 있는 가지수를 저장한다?
- 발생한 경우의 수를 인접노드라고 칠 수 있나
========================================
방문리스트의 개수 = 최대 N까지(어떤 경우의 수라도 -1의 경우의 수가 존재 최대 방문해도 N을 넘을 수는 없다.)
이미 방문했던 노드면 최단거리가 아닌 거지,,,,,,,,,,,,,,
=======================================
모든 노드는 -1을 뺀다는 경우의 수를 가진다.(인접노드로 -1 값을 가지게 됨.)
모든 경우의 수를 보고 최단 거리를 구해야 하므로 노드당 -1의 값을 선택하게 되는 경우를 queue에 추가해야 한다.
연산결과 값 하나하나를 노드로 보고 수가 등장하면 = 방문
"""
from collections import deque

# 10
N = int(input())

# 방문리스트
visited = [False] * (N + 1)

# 연산에 등장했던 수를 저장할 answer를 추가하고 나중에 return할 것
def bfs(start, answer):
    queue = deque()
    
    # 시작점과 시작점이 들어가 있는 리스트를 인자로 보내줌. (10, [10])
    queue.append((start, answer))
    while queue:
        v, answer = queue.popleft()
        # 이미 방문했던 노드라면(이미 이 루트는 최단거리가 아닌 거니까) => 외우자 그냥 받아들여
        # 다음 반복 시행
        if visited[v]:
            continue
        # while문 종료 조건 : 연산 결과가 1이면 종료
        if v == 1:
            print(len(answer) - 1)
            return answer
        
        # 3떨인 경우
        if not v % 3:
            
            # 3으로 나눈 몫(v), answer.append(3으로 나눈 몫)한 answer를 같이 인자로 전달
            # v가 9라면, queue.append(9 // 3, [..answer, 9 // 3])
            queue.append((v//3, answer + [v//3]))
            visited[v] = True
        
        if not v % 2:
            queue.append((v//2, answer + [v//2]))
            visited[v] = True
        
        # 3떨도 아니고 2떨도 아닌 경우 / -1의 모든 경우의 수를 봐야하기 때문에
        # v-1의 값도 queue에 추가
        queue.append((v-1, answer + [v - 1]))
        
print(*bfs(N, [N]))