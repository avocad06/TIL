# 17388

numbers = list(map(int, input().split()))
num_words = list(map(str, numbers))
# print(num_words)

if sum(numbers) >= 100:
    print("OK")
else:
    mn = min(numbers)
    loc = num_words.index(str(mn))
    if loc == 0:
        print("Soongsil")
    elif loc == 1:
        print("Korea")
    elif loc == 2:
        print("Hanyang")