# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# for 문

# 1부터 n 까지의 나열
# 하나씩 꺼내서 더해야할 result
# 0부터 계속 증가할 변수 num

chars = int(input())
result = 0

# range 범위에 있는 수를 다 돌아라
for num in range(chars):
    result = result + num
print(result)
    
    
    






# while 문
n = int(input())
a = 0
result = 0

while a <= n :
    result += a
    a += 1
print(result)
