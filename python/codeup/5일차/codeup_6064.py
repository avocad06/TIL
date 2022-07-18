#64

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
print((a if a<b else b) if((a if a<b else b))<c else c)
# a와 b 중에 a가 작으면 a, 그렇지 않으면 b
# 앞선 결과가 c보다 작으면 해당 결과 출력
# 그렇지 않으면 c