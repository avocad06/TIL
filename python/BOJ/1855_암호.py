# BOJ-1855

n = int(input())
n_lis = input()

code = []
# 열의 개수를 나눈 = 행의 개수
for i in range(len(n_lis)//n):
  code.append(n_lis[i*n:i*n+n]) # 곱하기가 무슨 뜻인가여?

for j in range(len(code)):
  if j % 2 == 1:
    code[j] = code[j][::-1]

a = len(code)
b = len(code[0])

for bb in range(b):
  for aa in range(a):
    print(code[aa][bb], end='')