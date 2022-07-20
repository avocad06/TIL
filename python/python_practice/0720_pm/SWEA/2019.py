
N = int(input())
# 1부터 주어진 횟수까지이므로, double의 초기값 1
double = 1

# N 까지 순회
for i in range(N+1):
    print(double, end=" ")
    double *= 2