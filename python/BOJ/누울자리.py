# 1652
"""
"""
import sys
sys.stdin = open("누울자리.txt")

room = [list(input()) for _ in range(int(input()))]
# print(room)
answer = [0, 0]
cnt = 0

for r in range(len(room)):

    for c in range(len(room[0])):
        
        seat = room[r][c]
        
        if seat == '.':
            cnt += 1
            # print(r,c)
        
        elif seat == 'X':
            if cnt >= 2:
                answer[0] += 1
                cnt = 0
                
            else:
                cnt = 0
                
    if cnt >= 2:
        answer[0] += 1
    cnt = 0    

# print(answer)
cnt = 0
for c in range(len(room[0])):

    for r in range(len(room)):
        
        seat = room[r][c]
        
        if seat == '.':
            cnt += 1
        
        elif seat == 'X':
            if cnt >= 2:
                answer[1] += 1
                cnt = 0
            
            else:
                cnt = 0
            
    if cnt >= 2:
        answer[1] += 1
    cnt = 0
        
print(*answer)