# 1543
import sys
sys.stdin = open("문서검색.txt")

words = input().replace(" ", "*")
target = input().replace(" ", "*")
# print(words,target)

new_words = words.split(target)
print(words, target, new_words)

print(len(new_words) - 1)