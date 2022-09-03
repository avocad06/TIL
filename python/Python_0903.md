# 이진탐색 기본

> 이진탐색 구현
>
> [BOJ 1920. 수 찾기]([1920번: 수 찾기 (acmicpc.net)](https://www.acmicpc.net/problem/1920))

```python
# 인자로는 리스트, 타겟, 시작과 끝의 인덱스가 필요
def bsearch (arr, target, left_, right_):
  
  # 시작 인덱스가 끝의 인덱스보다 크면 반복문을 종료
  while left_ <= right_:
    
    # 중간값은 시작과 인덱스의 합의 절반
    mid = (left_ + right_)//2
  
    # target이 arr[mid]와 같다면
    # 해당 숫자가 정렬된 리스트에 있다는 의미이므로
    # 해당 함수를 종료
    if target == arr[mid]:
      return 1
    
    # target이 arr[mid]보다 크다면
    # 시작 인덱스의 값을 중간값 + 1로 갱신
    # 중간값의 인덱스 이후를 찾아야하므로
    elif target > arr[mid]:
      left_ = mid + 1
    
    # target이 arr[mid]보다 작다면
    # 끝 인덱스의 값을 중간값 -1 로 갱신
    # 중간값의 인덱스 이전을 찾아야하므로
    elif target < arr[mid]:
      right_ = mid -1
      
  return 0
```

