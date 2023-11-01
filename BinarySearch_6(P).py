n, m = map(int,input().split())
# 각 떡의 개별 높이 입력
hei = list(map(int,input().split()))

start = 0
end = max(hei)
result = 0

# 이진 탐색
while(start <= end):
    total = 0
    mid = (start + end) // 2
    # 잘랐을 때 떡의 양 계산(total)
    for item in hei:
        if item > mid:
            total += (item-mid)
    # 떡의 양이 목표(m) 보다 적으면 끝 점 줄여서 더 많이 자르게
    if total < m:
        end = mid - 1
    # 목표보다 많으면 일단 result에 넣어놓고 덜 자르게 하면서 계속 갱신
    else:
        result = mid
        start = mid + 1

print(result)
