# n 입력
n = int(input())

# 리스트 선언 후 n개의 정수 저장
array = list()
for i in range(n):
    array.append(int(input()))

# 역으로 정렬
array = sorted(array, reverse=True)
print(array)