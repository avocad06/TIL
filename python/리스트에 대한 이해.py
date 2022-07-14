# int()는 숫자나 문자열을 정수 객체로 반환한다. 
# input().split()은 리스트의 형태인데
# 어떻게 각 요소에 대한 int함수가 적용되는가?

a, b = input().split()
print(type(a)), print(type(b))
# <class 'str'>
# <class 'str'>
print(type(input().split()))
# <class 'list'>

# 리스트 안의 구성 요소가 문자열이기 때문이다.
# 리스트 값 안에는 서로 다른 타입의 요소를 가질 수 있다.
my_list = [0, 's', True]
cnt = 0

for i in my_list:
    cnt += 1
    print(type(my_list[cnt-1]))
    
# <class 'int'>
# <class 'str'>
# <class 'bool'>