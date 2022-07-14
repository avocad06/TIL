# a 개수 구하기

#통(word)을 순회해서 'a'라는 문자를 만날 때마다 다른 통(cnt)에 넣겠습니다.
word = input()
cnt =0
for num in word :
    if 'a' == num :
        cnt += 1
print(cnt)
    

