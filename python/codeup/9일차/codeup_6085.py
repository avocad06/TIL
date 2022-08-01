# 6085.
"""
이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.

예를 들어
일반적인 1024 * 768 사이즈(해상도)의 각점에 대해
24비트(rgb 각각 8비트씩 3개)로 저장하려면
1024 * 768 * 24 bit의 저장공간이 필요한데,
1024*768*24/8/1024/1024 로 계산하면 약 2.25 MB 정도가 필요하다.
# 입력
w, h, b 가 공백을 두고 입력된다.
단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.

# 출력
필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
단, 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.

"""
w, h, b = map(int,input().split())
print(f'{format(w*h*b/8/1024/1024, ".2f")} MB')