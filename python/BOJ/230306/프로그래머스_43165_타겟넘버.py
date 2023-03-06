numbers= [1, 1, 1, 1, 1]

# 타겟 넘버를 만들 수 있는 방법의 수
answer = 0
target = 3
leaves= [0]

for num in numbers:
    tmp = []
    for parent in leaves:
        tmp.append(parent + num)
        tmp.append(parent - num)
        # print(parent)
    leaves = tmp
for leaf in leaves:
    if leaf == target:
        answer += 1