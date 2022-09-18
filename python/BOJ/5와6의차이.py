# 2864
"""
"""
words = input()
words_min = list(map(int, (words.replace('6', '5')).split()))
# print(words_min)
words_max = list(map(int, (words.replace('5', '6')).split()))
# print(words_max)
print(sum(words_min), sum(words_max))