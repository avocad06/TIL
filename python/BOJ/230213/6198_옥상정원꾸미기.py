""" 
1. 옥상 관리인은 오른쪽을 바라본다.
2. 내 빌딩 높이보다 높은 옥상은 확인할 수 없다. 그 이후도 못 한다.
3. 오른쪽 중에 제일 큰 수가 나타나면 확인할 수 있는 수를 초기화한다.
==================================================================
1. 옥상 관리인은 오른쪽을 바라본다. 오른쪽에 높은 수가 나타나면
2. 스택의 마지막 값을 기준으로 높은 수를 볼 수 있는지 판단하고,
3. 스택의 마지막값이 더 크다면 스택에 넣고,
4. 아니라면 뺀다.
5. 스택에 들어갈 값은 바인딩되어있는 건물을 볼 수 있는 다른 건물을 의미한다.
"""
N = int(input())

garden = []
for _ in range(N):
    garden.append(int(input()))
    
# print(garden)

# 지나온 수가 지금 나보다 크다
# 지나온 수는 나를 관찰할 수 있다.

result = 0
stack = []
for num in garden:
    while stack:
        # num이 stack[-1]보다 크면
        # num은 stack[-1] 건물이 볼 수 있는 건물로 +1
        if stack[-1] > num:
            break
        
        # num이 stack[-1]보다 작으면
        # stack[-1]건물이 볼 수 있는 건물은 0개
        # 가장 먼저 마주친 오른쪽(num)이 stack[-1]보다 크니까
        # 빼고 stack에 있는 이전 값으로 넘어가기(stack[-2, -3 ...])
        # 이런 식으로 stack을 순회하며 각 stack의 건물들이 num을 볼 수 있는지 확인 가능
        else:
            stack.pop()
            
    result += len(stack)
    stack.append(num)
    
print(result)