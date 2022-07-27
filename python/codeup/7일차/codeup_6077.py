# 6077.
"""
정수 1개를 입력받아 짝수의 합을 구해보자.

# 입력
정수 1개

# 출력
1부터 출력받은 수까지 짝수만 
합해서 출력

"""
# n = int(input())
# even_sum = 0
# for i in range(n + 1):
#     if i % 2 == 0:
#         even_sum += i
# print(even_sum)

n = int(input())
t = 0
even_sum = 0
while t <= n:
    if t % 2 == 0:
        even_sum += t
    t += 1
print(even_sum)
        