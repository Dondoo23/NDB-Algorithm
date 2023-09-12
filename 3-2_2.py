n, m, k = map(int, input().split()) # n, m, k 공백으로 구분하여 입력
data = list(map(int, input().split())) # n개의 수를 공백으로 구분하여 입력

data.sort()
print(data)

first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = first * k + second # 가장 큰 수를 k번곱하고 두번째 큰 수를 1번 더하는 규칙이 반복

if m % (k+1) == 0: # m이 k+1로 나누어떨어질 때
    result *= (m // (k+1)) # 규칙이 m을 k+1로 나눈만큼 반복
else: # 나누어 떨어지지 않을 때
    result *= (m // (k+1))
    result += (first * (m % (k+1))) # k+1로 나누고 난 나머지만큼 가장 큰 수를 더해줌

print(result)