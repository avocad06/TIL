# 5431.
"""
"""

import sys
sys.stdin = open("민석과제.txt")

for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    answer = []
    for num in range(1, N+1):
        if num not in submit:
            answer.append(num)
            
    print(f'#{t}', *answer)