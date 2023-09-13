n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어떨어지는 수가 될 때까지 1씩빼기
    target = (n//k) * k
    result += (n - target)
    n = target

    # N이 K보다 작아졌다면 탈출
    if n < k:
        break
    result += 1
    n //= k

# 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)