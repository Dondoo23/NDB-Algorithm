n = int(input())
arr = list(map(int,input().split()))
arr.sort()

result = set(arr)
new_arr = list(result)

sum = 0
for i in new_arr:
    count = arr.count(i)
    count = count // i
    sum += count

print(sum)