# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

 # 두 원소가 속한 집합 합치기   
def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# 노드의 개수와 간선의 개수
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# 모든 간선을 입력받을 리스트
edges = []
for _ in range(m):
    x, y, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 첫번째 원소를 비용으로 설정
    edges.append((cost, x, y))

# 간선을 비용순으로 정렬
edges.sort()

# 비용의 합을 내기 위한 result
result = 0
# 가장 큰 값을 구하기 위한 last
last = 0
for edge in edges:
    cost, x, y = edge
    # 사이클이 발생하지 않을때에만
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost
        last = cost

print(result - last)