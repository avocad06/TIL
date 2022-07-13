# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

numbers_count = 0 
# numbers에서 원하는 수 갯수 카운팅한 거
for num in numbers :
    # print(type(num)) #int
    if num == 5 :
        numbers_count += 1
print(numbers_count)

