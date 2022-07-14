# apple 역순으로 출력하기

word = 'apple'
word_count = 0
for i in word:
    word_count += 1
    
for y in range(word_count-1, -1, -1): 
    print(word[y], end="")

