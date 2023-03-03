""" 
1. 커서를 기준으로 왼쪽 스택과 오른쪽 스택으로 나눈다.
2. '>'가 들어오면 오른쪽 스택의 마지막 값을 왼쪽 스택에 붙이고
3. '<'가 들어오면 왼쪽 스택의 마지막 값을 오른쪽 스택에 붙이고(커서가 이동하므로)
4. '-'가 들어오면 왼쪽 스택의 마지막 값을 지운다.
"""


T = int(input())

for _ in range(T):
    left = []
    right = []
    pwd = input()

    for x in pwd:
        if x == ">":
            if right:
                left.append(right.pop()) 
        elif x=="<":
            if left:
                right.append(left.pop())
        elif x=="-":
            if left:
                left.pop()
        else:
            left.append(x)

print("".join(left)+"".join(reversed(right)))