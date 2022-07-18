#58

a, b = input().split()
a, b = bool(int(a)), bool(int(b))
print(not(a or b))

# a와 b가 not a and not b 여야만 하므로
