result={}
# result는 현재 빈 딕션
# 아무런 키도 없는 상태
result['a']=1
result['a'] += 1
# NameError: name 'a' is not defined

print(result)

# if char in result 
# # 만약 result에 키가 있으면,
# result[char]=0
# # result 의 value 는 0이다.

# else:
# # 만약 result에 키가 없으면,
# result[char]=result[char]+1
# result의 value에 1을 추가한다.
# => 이거 자체로 딕셔너리가 생성됨.
# 생성 됐는데 키가 없으니까 값을 추가할 수도 없음.=>error

# 기존 reulst 키에 대응하는 value에 값을 추가해야되는데, key가 없어서.
# 추가를 못한다. => 에러 okey 이해했음.
# ===========================
# result[char]의 초기값을 1로 한다.
# 위의 오류에서는 값을 추가할 키값을 찾지 못해서 오류가 났는데, 
# result[char]=1을 수행할때에는 키는 자동으로 생성됐다 가정하고, 수행하는 거인가 ?
# => 당연함. result[char]=1 자체가 char이라는 키의 값을 1로 정의하겠다는 뜻임.

# .get메서드를 사용한 풀이
# 딕셔너리를 풀다보녀 키가 없다는 에러 메시지를 많이 볼 수 있다.
