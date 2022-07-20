# 예제 08. [오류 해결] 과일 개수 구하기

#오류코드
word = "HappyHacking"

count = 0

for char in word:
    # if char == "a" or "e" or "i" or "o" or "u":
    # 오류 원인
    # char에 바인딩된 word는 "HppyHacking" 문자열 한 개 이므로
    # 해당 문자열에 모음이 있는지만 확인하면 된다.
    if char in 'aeiou':   
        count += 1

print(count)