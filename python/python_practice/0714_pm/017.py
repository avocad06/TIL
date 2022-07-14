# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# ord('a') #97 문자에 대응하는 숫자
# chr(97) # 'a' 숫자에 대응하는 문자

# 일단 순회하면서 모든 문자를 숫자에 대응합니다
# 그리고 그 숫자로 list를 만들어서
# 숫자 list를 순회하며 해당 문자를 대문자의 유니코드로 바꿉니다.
# 출력합니다.


word = input()
result =[]
for char in word:
    char = ord(char)-32
    result += [char]
    for num in result:
        num = chr(num)
    print(num,end="")
    