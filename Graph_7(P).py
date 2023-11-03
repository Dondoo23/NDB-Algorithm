# n은 학생번호 m은 연산입력 개수
n, m = map(int, input().split())

parent = []
for i in range(n+1):
    parent.append(i)

# 팀 합치기
def union(parent, a, b):
    if parent[a] < parent[b]:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

# 같은 팀인지 확인
def check(a, b):
    if parent[a] == parent[b]:
        print('YES')
    else:
        print('NO')

# 연산 입력받아 0이면 팀합치고 1이면 같은팀인지 확인
for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(parent, a, b)
    elif cal == 1:
        check(a, b)
