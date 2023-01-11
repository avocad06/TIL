def make_array(N):
    array = [False, False] + [True for _ in range(N - 1)]
    
    for idx in range(2, int(N ** 0.5) + 1):
        if array[idx]:
            j = 2
            while idx * j <= N:
                array[idx * j] = False
                j += 1
    
    return array

# 100반까지의 소수를 모두 판별해놓는다
prime_array = make_array(10 ** 6)



for _ in range(int(input())):
    N = int(input())
    result = 0
    # 제곱근을 기준으로 대칭인 약수의 성질처럼
    # 요소의 중복을 피하기 위해 두 수의 합에서도 반만 돈다
    # 근데 원리는 모르겠다
    for num in range(2, int(N * 0.5) + 1):
        if prime_array[num] and prime_array[N-num]:
            result += 1
            
            # 확인용 코드
            # result.append((num, N - num))
            
    print(result)
