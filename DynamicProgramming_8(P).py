# n가지 종류의 화폐, 가치의 합이 m원이 되도록
n, m = map(int,input().split())

# n개의 화폐 정보 입력
coin = []
for i in range(n):
    coin.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
count = [10001] * (m+1)
count[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        if count[j-coin[i]] != 10001: # i-k 원을 만드는 방법이 존재하는 경우
            count[j] = min(count[j], count[j-coin[i]]+1)

if count[m] == 10001: # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(count[m])