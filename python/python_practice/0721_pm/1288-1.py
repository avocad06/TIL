import sys
sys.stdin = open("1288_input.txt", "r")

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
            # 문자열의 i번째 인덱스의 값을 인덱스로 하고 
            # 해당 인덱스의 값에 1을 추가한다.
            # i가 0일 때, num[0]번째 인덱스의 값(문자)을
            # ex) num = '1295'일 때,
            # 다시 리스트 numbers의 인덱스 numbers[1]로 받아와서
            # 해당 인덱스의 값에 1을 더한다.
            count += 1
        # 해당 반복이 끝나면 시행횟수 1 증가하고
        # 다시 numbers 리스트에 0이 없을 때까지 반복
    print(f'#{test_case} {num}')