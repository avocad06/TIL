# 1218
"""
"""
import sys
sys.stdin = open("괄호짝.txt")

for t in range(1, 11):
    print(f'#{t}', end=" ")
    l = int(input())
    words = input()
    # print(words)
    open_ = []
    close_ = 0
    check = 0
    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    cnt = 0
    for word in words:
        # 여는 괄호가 나왔을 때
        if word in opens:
            open_.append(word)
            cnt += 1
            # print(open_)

        elif word in closes:
        # 닫히지 않은 괄호가 있을 때
            if open_:
                n = opens.index(open_[-1])
                m = closes.index(word)
                # print(cnt, word, open_[-1], n, m)
                if n == m:
                    open_.pop()
                
                else:
                    print(0)
                    check += 1
                    break
                
            elif not open_:
                close_ += 1
                print(0)
                check += 1
                break
            
    if not open_ and close_ == 0:
        print(1)
        
    elif not check:
        print(0)

