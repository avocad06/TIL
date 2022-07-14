# 문자열에서 a 가 처음으로 등장하는 위치를 출력해주세요. a가 없는 경우에는 -1을 출력
# word를 순회해서 'a'와 만나면 반복을 중지합니다.
# a를 만나기까지 순회한 횟수를 세는 통을 만들고
# 통의 숫자를 a가 처음으로 등장하는 위치-1의 인덱스[]에 대입합니다.
# cnt 는 word[cnt] 가 될 거라서 0부터 시작하는 게 맞다.


word = input()
cnt = 0

if 'a' in word :
    for num in word:
        cnt += 1
        if num == 'a':
           break
    print(cnt-1)

elif 'a' not in word :
    print('-1')
    

    

    