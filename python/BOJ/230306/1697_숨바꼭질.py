# 1697번 숨바꼭질

from collections import deque

# 입력값 받기
n, k = map(int, input().split())
# 움직일 수 있는 최대 좌표는 100000
max_num = 100000
# 해당 위치에 도착했을 때 시간을 표시하는 리스트
visited = [0] * (max_num + 1) # 현재는 시작하지 않았기에 0으로 모두 초기화

# bfs 함수 정의
def bfs():
    q = deque()
    # 수빈이 출발점 위치 큐에 삽입
    q.append(n)
    while q:
        x = q.popleft()
        # 수빈이 위치가 동생의 위치와 같다면 반복문 종료
        if x == k:
            # print(visited[x])
            break
        # 이동할 수 있는 방향에 대하여
        for j in (x-1, x+1, x*2):
            print(j)
            # 주어진 범위 내에 있고 아직 방문하지 않았다면
            if 0 <= j <= max_num and not visited[j]:
                # 이동한 위치에 현재 이동한 시간 표시
                visited[j] = visited[x] + 1
                # 큐에 추가
                q.append(j)
            break
# bfs 실행
bfs()