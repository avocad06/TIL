#34
a, b = input().split()
print(type(input().split()))
print(a), print(b)
print(type(a),type(b))
c = int(a) - int(b)
print(c)

#리스트는 정수로 형 변형이 안 된다?
# 안된다. 어떤 함수든 모든 요소에 적용시켜주는 함수 map을 이용하여 변환할 수는 있다.