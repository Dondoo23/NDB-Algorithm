n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 # 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도가 낮은 순서부터 하나씩 확인
    count += 1 # 현재 그룹에 해당 모험가 포함시키기
    if count >= i: # 그룹에 포함된 모험가의 수가 공포도 이상이면 그룹결성
        result += 1 # 총 그룹의 수 1 증가
        count = 0
print(result)