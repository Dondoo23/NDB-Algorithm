#N,M,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
data.sort()

first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0: # m이 0이면 반복문 탈출
            break
        result += first
        m -= 1 # 더할때마다 1씩 빼기
    if m == 0:
        break
    result += second
    m -= 1

print(result)