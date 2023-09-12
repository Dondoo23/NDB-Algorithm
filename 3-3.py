n, m = map(int, input().split()) # n, m을 공백으로 분리하여 입력

max_value = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) # 현재 줄에서 가장 작은 수
    max_value = max(max_value, min_value) # 가장 작은 수들 중에서 가장 큰 수 찾기

print(max_value)