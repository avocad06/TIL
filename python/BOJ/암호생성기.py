# 1225
"""
"""
import sys

sys.stdin = open("암호생성.txt")
from collections import deque

for _ in range(10):
    
    t = int(input())
    
    word = list(map(int, input().split()))
    # print(word)
    words = deque(word)
    # print(words)

    # 반복때마다 감소시켜야할 수
    cnt = 1
    while True:
        if words[-1] == 0:
            break
        # 한 사이클
        cnt = cnt % 5
        if cnt == 0:
            cnt = 5
        cur = words.popleft()

        check = cur - cnt
        if check < 0:
            words.append(0)
            break
        words.append(check)
        cnt += 1

    print(f'#{t}', *words)
