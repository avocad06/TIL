wyw = [0] * 10 ** 7

for num in range(5, 9999999):
    num = str(num)
    if num == num[::-1]:
        wyw[int(num)] = num

def is_prime(n):
    n = int(n)
    for num in range(2, int(n ** 0.5) + 1):
        if not n % num:
            return 0
    else:
        return str(n)

# print(wyw)
a, b = map(int, input().split())
for idx in range(a, b + 1):
    if idx > len(wyw) - 1:
        break
    
    if wyw[idx] and is_prime(idx):
        print(idx)

print(-1)