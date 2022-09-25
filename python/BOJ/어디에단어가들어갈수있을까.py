# 1979
""" 
"""
from pprint import pprint
import sys
sys.stdin = open("단어어디.txt")

for t in range(1, int(input()) + 1):

    N, K = map(int, input().split())

    puzzle = [input().split() for _ in range(N)]
    # pprint(puzzle)

    answer = 0

    # 행 우선 순회
    for r in range(N):
        # 행이 바뀔 때마다 cnt를 초기화
        cnt = 0
        
        for c in range(N):
            
            cur = puzzle[r][c]
            if cur == '1':
                cnt += 1
                
            #puzzle[r][c]가 0이라면 cnt초기화
            elif cur == '0':
                if cnt == K:
                    answer += 1
                cnt = 0
            
        if cnt == K:
            answer += 1
        

    for c in range(N):
        
        cnt = 0
        
        for r in range(N):
            
            cur = puzzle[r][c]
            if cur == '1':
                cnt += 1
                
            elif cur == '0':
                if cnt == K:
                    answer += 1
                cnt = 0
                
        if cnt == K:
            answer += 1

    print(f'#{t} {answer}')