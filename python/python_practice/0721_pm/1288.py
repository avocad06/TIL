import sys
sys.stdin = open("input/1288.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = [0] * 10
# print(result) 0이 10개인 리스트 생성
    sheep_cnt = 1
    # 시행횟수
    while 0 in result:
        # 0이 result에 계속 있을 동안 반복
        num = str(N * sheep_cnt)
        # 시행횟수 * N을 문자로 형 변환
        # 그럼 이제 해당 문자를 순회해야 그 글자가 있는지 없는지 result랑 비교할 수 있겠지(x)
        # 이 접근이 아니고 있는 글자만 계속 카운팅 해서
        # 0의 값을 가지는 인덱스가 없을 때까지 반복
        for i in range(len(num)):
            # reulst의 0이 없어지려면,
            # 리스트의 몇 번째 인덱스의 값이 0이 아니면 되는 거지.
            # 리스트의 인덱스를 0~9까지의 번호표로 가져오는 거랑 마찬가지
            # 리스트의 인덱스가 문자열의 숫자랑 일치하면,
            # 해당 인덱스의 값을 1씩 증가시킨다.
            # 리스트의 인덱스는 result[]이고,
            # 문자열의 숫자는 num[]이고, 현재 i 는 num의 길이만큼 순회중
            # i가 순회하고 있는 문자열의 인덱스를 리스트의 인덱스에 넣어버리면,
            
            # N이 '1295'로 주어졌을 때, num[0]='1'이고 이 '1'이 리스트의 인덱스랑 일치하려면,
            # result[int(num[i])]의 형태가 되면 된다. 이때 '1'은 문자이므로 정수 형 변환 필요.
            # 현재 result[1] 의 값은 0이지만, 리스트 인덱스와 문자열의 숫자가 일치하므로,
            # 해당 인덱스의 값을 1 증가시킨다. result[int(num[0])] += 1
            result[int(num[i])] += 1
            # 문자열 카운팅이 끝났으면
        # 시행 횟수 증가
        sheep_cnt += 1
        # 미리 증가해 놔야 문자열 num에 정상 반영됨.
    print(f'#{test_case} {num}')
        