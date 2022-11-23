# 1526
""" 
"""
import sys
sys.stdin = open("가장큰금민수.txt")
# print(int(input()))

for num in range(int(input()), 3, -1):
        check = set()
        for word in list(str(num)):
            check.add(int(word)) # 9
        if check == {4} or check == {7} or check == {4, 7}:
            print(num)
            break