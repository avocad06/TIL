# 6072.
"""
정수 1개가 입력되었을 때 카운트다운을 출력

# 입력
정수 1개 입력

# 출력
1만큼 줄이면서 한줄에 1개씩 카운트다운

"""

N = int(input())
while N != 0:
    # N이 0이 될 때까지 N을 1개씩 줄여가며 출력
    print(N)
    N -= 1
