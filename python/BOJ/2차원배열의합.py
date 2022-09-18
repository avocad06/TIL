# 2167
"""
어떤 배열의 a의 a[i]에서 a[j]까지의 합은 a[0]에서 a[j]까지의 합에서 a[0]에서 a[i-1]까지의 합을 뺀 결과와 같다.
값을 입력받음과 동시에 요소들의 합을 구해놓고 어떤 요청에 대해 단순히 두 요소의 차를 구하는 방식으로
시간 복잡도를 줄일 수 있을 것으로 본다.
어떻게?
"""
import sys
sys.stdin = open("2차원배열.txt")

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
# print(matrix)

K = int(input())
for _ in range(K):
    answer = 0
    i, j, x, y = map(int, input().split())
    
    for r in range(i-1, x):
        for c in range(j-1, y):
            answer += matrix[r][c]
            
    print(answer)