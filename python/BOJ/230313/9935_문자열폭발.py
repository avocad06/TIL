# 9935

""" 
initial Idea:
err - 문자열이 일치할 때만 폭발하는 것을 몰랐음
1. 순회 중인 문자가 폭발 문자열 중 하나라면, 폭발 문자열 후보를 담아놓는 checkList라는 스택에 추가하자
2. 이어지는 문자가 폭발 문자열인지 아닌지 판단하려면 다음 문자를 확인해야 하는데, 어떻게 해야 하지?
3. 멀리 떨어진 C랑 4가 있었다면 어떻게 다시 정답 문자열에 넣지?

solution:
1. 우선 문자열은 정확히 일치할 때 폭발함
2. 문자열을 순회하며 stack에 넣고 현재 문자가 폭발 문자열의 마지막 문자와 일치한다면,
=> 폭발 문자열과 정확히 일치해야 하기 때문에 마지막 글자를 확인(다음 글자가 폭발일지 아닐지 확인 안해도 됨)
3. 폭발 문자열의 길이만큼 역슬라이싱한 값이 폭발 문자열과 일치한다면,
4. stack에서 해당 범위만큼의 문자열 요소를 삭제함.(예약어 del 사용)
"""

# 입력값 받아오기
S = input()
bomb = list(input())

stack = []
for char in S:
    stack.append(char)
    
    if char == bomb[-1] and stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]
        
if stack:
    print("".join(stack))
    
else:
    print("FRULA")
    
    
