# 6072.
"""
영문 소문자 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력

# 입력
영문자 1개가 입력

# 출력
a부터 입력한 문자까지 순서대로 공백을 두고
한 줄로 출력한다.

"""

c = ord(input())
t = ord('a')
while t <= c:
    # t의 값이 입력한 문자의 정수값이 될 때까지 반복
    print(chr(t), end=" ")
    t += 1
    # 지금의 t값을 출력한 다음에 다음 t로 이동한다.