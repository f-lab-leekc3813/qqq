def binary_search(array, target, start, end):
  # 범위 넘어갈시 종료
  if start > end:
    return None
  # 중간값
  mid = (start + end) // 2
  # 찾은 경우 중간값 인덱스 반환
  if array[mid] == target:
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] < target:
    return binary_search(array, target, start, mid - 1)
  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, target, mid + 1, end)

# n(가게의 부품 개수)입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int,input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

m = int(input())
x = list(map(int,input().split()))

for i in x:
  result = binary_search(array, i, 0, n-1)
  if result !=None:
    print('yes', end = ' ')
  else:
    print('No', end = ' ')