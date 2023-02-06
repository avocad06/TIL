""" 
1. 스택을 사용하면 이미 자신의 오큰수를 발견한 수들을 스택에서 빼준다.
2. 각 원소들을 딱 2번씩만스캔할 수 있다.
3. while문 맨 처음 시행은 넘어간다.
4. stack을 언제 비워줄 것인가?
"""

N = int(input())
arr = list(map(int, input().split()))

answer = [-1] * (N + 1)

stack = []
for tup in enumerate(arr, 1):
    # index가 더 앞에 온다.[0]
    # 지나 온 (나보다) 작은 수를 넣는 stack
    while stack:
        # stack의 가장 마지막이 현재 바인딩된 수보다 작다면(오큰수)
        if stack[-1][1] < tup[1]:
            answer[stack[-1][0]] = tup[1]
            stack.pop()
        else:    
            break
    stack.append(tup)
        
print(*answer[1:])