# a의 모든 위치 출력하기

# 통을 순회하다가 'a'를 만나면 해당 회차를 통에 넣기, 못 만나면 그냥 계속 순회하기

word = input()
cnt = 0

for num in word:
    cnt += 1
    if num != 'a':
        continue
    print(cnt-1, end=" ")
        