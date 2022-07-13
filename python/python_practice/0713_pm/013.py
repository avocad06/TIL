#주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
word = 'apple'
word_count = 0
for num in word:
    word_count += 1
for i in range(word_count-1,-1,-1): 
    print(word[i], end="")