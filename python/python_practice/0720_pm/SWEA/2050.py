import sys
sys.stdin = open('SWEA_txt/2050.txt', "r")

#ABCDEFGHIJKLMNOPQRSTUVWXYZ

# 1. 나의 접근 방법
# input 값을 순회하면서 등장하는 알파벳 : 순회 값에 매칭하는 딕셔너리 생성
# 해당 딕셔너리와 input값의 알파벳을 비교하여 매칭

word = input()
dict = {}
cnt = 0

for i in word:
    if i not in dict:
        cnt += 1
        dict[i] = cnt
        
for match in word:
    print(dict[match], end=" ")
    
# 실행 결과 : 실패
# 원인 : apple 을 넣었을 때 기대한 p의 알파벳 순서가 아닌 등장 순서로 매칭
# apple # 1 2 2 3 4 
print('==============================================================')

# 2. 코드리뷰 및 새로 접근
# 딕셔너리로 접근하지 말고, 아스키 코드와 유니코드 값으로 접근
# 문자를 입력받아 10진수 유니코드 값으로 변환하며 출력

word = input()
for char in word:
    # 아스키코드 값으로 A는 65
    # 출력값 1을 위해 -64 로 조작
    print(ord(char)-64, end=" ")
    
# 실행 결과 : 성공