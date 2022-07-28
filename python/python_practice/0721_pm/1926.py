

# # 문제 1926. 간단한 369게임

# '''문제
# 1. 숫자 1부터 순서대로 차례대로 말하되, 3,6,9가 들어가 있는 수는 말하지 않는다.
# "3", "6" "9"가 들어가 있는 수를 말하지 않는 대신, 박수를 친다.
# 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.
# 박수를 한 번 칠 때는 - 이며, 박수를 두 번 칠때는 - -가 아닌 --이다.

# 입력
# 정수 N

# 출력
# 1~N 까지의 숫자를 게임 규칙에 맞게 출력

import sys
sys.stdin = open("input/1926.txt", "r")


N = int(input())
clap_list=['3', '6', '9']
i_word = []
count = 0
for i in range(1, N+1):
    i_word += [str(i)]
    if i_word in clap_list:
        count += 1
print(count)
    
 
                
            
            