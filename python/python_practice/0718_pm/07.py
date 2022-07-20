# 예제 07. [오류 해결] 평균 구하기

# 오류코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    
# 오류원인
# 변수 count의 들여쓰기 for 문에 포함 되어 있지 않습니다.
# 연산자 '/'는 나누기 후 몫과 나머지를 출력하고, '//'는 몫만 출력합니다.
    count += 1
    
print(total / count)
    
    






