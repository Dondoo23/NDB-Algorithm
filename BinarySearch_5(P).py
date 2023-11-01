# 가게 물건의 개수
N = int(input())
# 가게 모든 물건들의 번호
store = list(map(int,input().split()))
# 고객이 찾는 물건의 개수
M = int(input())
# 고객이 찾는 모든 물건들의 번호
cust = list(map(int,input().split()))

# 고객들이 찾는 물건들을 하나씩 돌리면서 가게에 있다면 yes 없으면 no
for item in cust:
    if item in store:
        print('Yes')
    else:
        print('No')
