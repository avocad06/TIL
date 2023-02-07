""" 
1. 리스트는 유지해야할 것 같다.
2. 바인딩된 수가 위치한 인덱스 이하의 수들을 스택에 넣고,
3. while stack 동안 빼서 바인딩된 수와 크기를 비교
4. 가장 큰 수면 그 수는 무조건 0아냐 ?
5. 그럼 [0] * n 만큼 리스트를 만들어놓자.
6. list.index() 메서드 사용

======
시간초과
"""

N = int(input())
tower = list(map(int, input().split()))

answer = [0] * (N + 1)

stack = []
    # index가 더 앞에 온다.[0]
for tup in enumerate(tower, 1):
    # 지나 온 (나보다) 작은 수를 넣는 stack
    while stack:
        # stack의 가장 마지막이 현재 바인딩된 수보다 작다면(오큰수)
        if stack[-1][1] > tup[1]:
            answer[tup[0]] = stack[-1][0]
            break
        else:    
            stack.pop()
    stack.append(tup)
        
print(*answer[1:])