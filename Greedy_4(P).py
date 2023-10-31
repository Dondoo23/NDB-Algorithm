N, K = map(int, input().split())
count = 0
while True:
    count += 1
    if N % K == 0:
        N //= K
    else:
        N -= K
    
    if N == 1:
        break

print(count)