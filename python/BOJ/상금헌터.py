# 15953
"""
"""
import sys
sys.stdin = open("상금헌터.txt")

money_1 = {
    1 : 500,
    2 : 300,
    3 : 200,
    4 : 50,
    5 : 30,
    6 : 10
}

rewards1 = [0]
for idx in range(1, 7):
    rewards1 += [idx] * idx
# print(rewards)

money_2 = {
    1 : 512,
    2 : 256,
    3 : 128,
    4 : 64,
    5 : 32
}
rewards2 = [0]
for idx in range(5):
    rewards2 += [idx + 1] * 2 ** idx
# print(rewards2)

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if 1 <= a <= 21:
        a = money_1[rewards1[a]]
    else:
        a = 0
            
    if 1 <= b <= 31:
        b = money_2[rewards2[b]] 
    
    else:
        b = 0
        
    print(int(str(a + b) + '0000'))