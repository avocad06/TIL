# 10872
# 0! 은 1이므로
result = 1
# n이 0이어도 0!이 1이므로
for num in range(1, int(input()) + 1):
    result *= num
    
print(result)