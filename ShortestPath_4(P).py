INF = int(1e9)
# 노드의 개수 및 간선의 개수 입력
n, m = map(int,input().split())
# 2차원 리스트 만들고 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신으로 가는 비용은 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 비용을 1
for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 경유지와 목적지 입력
x, k = map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1,n+1):
    for j in range(1,n+1):
        for r in range(1,n+1):
            graph[j][r] = min(graph[j][r], graph[j][i]+graph[i][r])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)