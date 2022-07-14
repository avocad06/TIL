# 42

# format(수, ".2f")를 사용하면 
# 소수점 아래 3번째 자리에서 반올림하여 
# 소숫점 이하 두 번째 자리인 실수를 만들어준다.

a = input()
a = float(a)
# print(format(a, 2f))
# $ D:/python.exe c:/Users/user/Desktop/TIL/python/codeup/4일차/codeup_6042.py
#   File "c:\Users\user\Desktop\TIL\python\codeup\4일차\codeup_6042.py", line 6
#     print(format(a, 2f))   
#                      ^     
# SyntaxError: invalid syntax 
# format(수,"'.'출력하고자 하는 자릿수'f")의 형태가 아니라서 오류
print(format(a, ".2f"))