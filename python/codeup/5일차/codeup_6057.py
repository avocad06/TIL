#57

a, b = input().split()
a, b = bool(int(a)), bool(int(b))
print((a and b) or ((not a) and (not b)))

# a, b의 두 불린어가 같으려면, 둘이 같거나
# not a 와 not b(a와 b의 값을 반대로)가 같아야 함.