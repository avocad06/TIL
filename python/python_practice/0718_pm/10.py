# 예제 10. [오류 해결] 더 큰 최댓값 찾기

# 오류코드
number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)
# 오류원인
# TypeError: 'int' object is not callable
# 정수형은 호출할 수 없습니다.
# 변수 'max'에 할당된 정수형과 함수로 호출된 max의 충돌

max_num = max(number_list)
number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max_num > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max_num < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

