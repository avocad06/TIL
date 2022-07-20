import sys
sys.stdin = open('2050.txt', "r")

#ABCDEFGHIJKLMNOPQRSTUVWXYZ

word = input()
len(word) <= 200
dict = {}
cnt = 0

for i in word:
    if i not in dict:
        cnt += 1
        dict[i] = cnt
    elif i in dict:
        
for match in word:
    print(dict[match], end=" ")