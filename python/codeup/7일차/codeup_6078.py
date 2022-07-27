# 6078.
"""
소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# 입력
문자들이 1개씩 계속해서 입력

# 출력
영문 소문자 'q'가 입력될대까지 입력한 문자를 계속 출력

"""
import sys
sys.stdin = open("6078.txt")

while chr != 'q':
    chr = input()
    print(chr)