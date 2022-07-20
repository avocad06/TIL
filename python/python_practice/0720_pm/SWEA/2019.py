
N = int(input())
# 1부터 주어진 횟수까지이므로, double의 초기값 1
double = 1

# N 까지 순회
for i in range(N+1):
    print(double, end=" ")
    double *= 2
    
 =======================================================   
 # 수를 돌면서 이전 값에 2를 계속 곱해 나가는 것은
 # 제곱과 같다. 2의 0승, 2의 1승, ...
 # 즉, 2**바인딩된 수 로 표현할 수 있다.   
n = int(input())
for i in range(n+1):
    print(2**i, end=' ')