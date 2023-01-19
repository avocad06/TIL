from pprint import pprint

# 홀수인 자연수 N이 주어지면 N ** 2까지의 자연수를 달팽이 모양으로 채울 수 있다.
# 달팽이 모양을 위해 회전 방향을 바꾸는 횟수는
# 2 * N -1회
# 달팽이 모양의 회전 방향(하 우 상 좌)을 나타내는 좌표
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 맨 처음 회전 방향은 '하' (dr[0], dc[0])이지만 이후 식 전개를 위해 -1부터 시작
d = -1

N = int(input())
target = int(input())

snail_array = [[0] * N for _ in range(N)] + [[0, 0]]

# 시작 값
k = N ** 2

r, c = -1, 0

# 달팽이의 전체 회전만큼 반복
for _ in range(2 * N - 1):
    # 0번째 인덱스부터 시작
    d = (d + 1) % 4
    
    # 채워야 하는 N만큼 dr[d], dc[d]의 방향으로 진행
    for _ in range(N):
        r += dr[d]
        c += dc[d]
        snail_array[r][c] = k
        
        if k == target:
            snail_array[-1][0] = r + 1
            snail_array[-1][1] = c + 1
        
        k -= 1

    
    # 만약 d가 0이나 짝수 번째 인덱스라면, = 하 상 방향 진행
    if not d or not d % 2:
        N -= 1

# pprint(snail_array)
for arr in snail_array:
    print(*arr)