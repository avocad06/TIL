""" 
1. dp 는 이전에 저장된 값이다.
2. dp에는 이전 수의 최단 경로가 저장되어 있다.
3. dp[1] = 0이다.
4. 수가 반복됨에 집중할 것. 
"""


dp = [0, 0] + [0] * (10 ** 6 -1)
for n in range(2, 10 ** 6 + 1):
    dp[n] = dp[n - 1] + 1
    if not n % 2:
        dp[n] = min(dp[n], dp[n//2] + 1)
    
    if not n % 3:
        dp[n] = min(dp[n], dp[n//3] + 1)

N = int(input())
print(dp[N])