# 16953
from collections import deque

A, B = map(int, input().split())
# print(A, B)

answer = -1
queue = deque()
# 저장할 때 차수를 저장해놓으면 계속 누적해서 기록할 수 있다.
queue.append((A, 1))
while queue:
    # print(queue)
    node, cnt = queue.popleft()
    if node == B:
        answer = cnt
        break
    
    if node * 2 <= B:
        queue.append((node * 2, cnt + 1))
    if int(str(node) + '1') <= B:
        queue.append((int(str(node) + '1'), cnt + 1))
        
print(answer)