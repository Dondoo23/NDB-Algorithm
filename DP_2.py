# 정수 n 입력
n = int(input())
# 모든 식량 정보 입력
k = list(map(int,input().split()))

# 앞서 계산된 결과를 저장하기 위한 dp테이블
d = [0] * n

# 다이나믹 프로그래밍 진행
d[0] = k[0]
d[1] = max(k[0],k[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+k[i])

print(d[n-1])
