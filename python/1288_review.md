1. 지금까지 본 숫자들을 저장할 리스트 만들기
2. 값을 0으로 해서 리스트 안에 0이 없어지면 반복 중지
3. 리스트랑 비교할 문자열
   1. 시행횟수 * N을 문자열로 형 변환
   2. 문자열을 순회하며 해당 숫자를 인덱스로 가진 리스트에 1을 더한다.
4. 0이 없어지면 그 시점의 시행횟수 * N 출력

```python
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = [0] * 10
# 0을 10개 포함하는 리스트를 생성
    count = 1
    # 몇 번 시행했는지 초기값
    while 0 in numbers:
        # 리스트 안에 0이 없을 때까지 반복 실행
        num = str(N * count)
        # count번째 N의 문자열 형 변환
        for i in range(len(num)):
            # count번째 N 을 길이만큼 순회하면서
            numbers[int(num[i])] += 1
            # num의 i번째 인덱스의 값을 
            # 다시 numbers의 인덱스로 받아 그 값에 1을 더한다.
        count += 1
        # 해당 반복이 끝나면 시행횟수 1 증가하고
        # 다시 numbers 리스트에 0이 없을 때까지 반복
    print(f'#{test_case} {num}')
```

