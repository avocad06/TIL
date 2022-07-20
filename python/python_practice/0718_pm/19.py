# 문제 19. 숫자의 길이 구하기

number = 123

# 만약 123이 100이상이라면 세 글자일 것이다.
# 10 미만>0 이라면 output 은 한 글자
# 0의 개수가 늘어날 때마다 count 1

def ari(number):
    zero_cnt = 1
    n = 1
    if 0 < number <= 9:
        zero_cnt = 1
    while 10**n <= number :
        zero_cnt += 1
        n += 1
    
    
   
    
    return zero_cnt

print(ari(number))