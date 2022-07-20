text = ['원영', '유진', '유진', '리즈', '이서', '이서']
# 리스트업
ive = {}
# 아이브는 딕셔너리
for dive in text :
    # text를 돌면서
    ive[dive] = ive.get(dive, 0) + 1
    # dive에 바인딩된 key의 value는 
    # 아이브 딕셔너리에 'dive에 바인딩된 key'가 있으면, 해당 key의 'value'로 하겠습니다. 
    # 없으면, 해당 key의 값은 0으로 하겠습니다.
    # 글자의 등장 횟수니까 바인딩되는 글자는 무조건 1글자는 있음. 
    # = 한번 돌때마다 1은 추가해야된다는 것.(해당 글자는 무조건 하나는 있으니까.)
upper = sorted(ive.items())
ive = dict(upper)
print(ive,type(ive))
for i in ive: 
    print(i, ive[i])