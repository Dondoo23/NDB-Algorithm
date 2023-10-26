n, k = map(int, input().split())
A = list()
B = list()

A = list(map(int, input().split()))

B = list(map(int, input().split()))

for i in range(k):
    # A리스트의 가장 작은 값 인덱스
    index_a = A.index(min(A))
    # B리스트의 가장 큰 값 인덱스
    index_b = B.index(max(B))
    #서로 바꿔줌
    A[index_a], B[index_b] = B[index_b], A[index_a]

print(sum(A))