# 예제 09. [오류 해결] 과일 개수 구하기

# 오류코드
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        # fruit_count = {fruit: 1}
        # 오류 원인
        # fruit에 바인딩 된 키-값 쌍을 더해나가는 것이 아니라
        # fruit값만 바뀌게 됩니다.

    # else:
    #     fruit_count[fruit] += 1


# pprint(fruit_count)

        fruit_count[fruit] = 1
    else :
        fruit_count[fruit] += 1
        
pprint(fruit_count)