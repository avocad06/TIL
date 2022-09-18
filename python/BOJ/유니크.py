# 5533
"""
"""
import sys
sys.stdin = open("유니크.txt")

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
# print(game)

score = [[] for _ in range(len(game[0]))]
# print(score)

for c in range(len(game[0])):

    for r in range(len(game)):
        score[c].append(game[r][c])
# print(score)

answer = [0] * len(score[0])
# print(answer)

for r in range(len(score)):
        rnd = score[r]
        for c in range(len(score[0])):
            unique = score[r][c]
            if rnd.count(unique) == 1:
                answer[c] += unique
                # print(answer)
                
print(*answer, sep = '\n')       
    