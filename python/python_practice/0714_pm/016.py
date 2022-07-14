# 해당 문자열에서 모음의 갯수를 출력하기(모음 : a,e,i,o,u)

word = input()
cnt=0

for char in word:
    if char in 'aeiou':
        cnt += 1
print(cnt)