n = int(input())
plan = list(input().split())
row_count = 0
col_count = 0

size = len(plan)
for i in range(size):
    if plan[i] == 'r':
        if row_count < n-1:
            row_count += 1
    elif plan[i] == 'l':
        if row_count > 0:
            row_count -= 1
    elif plan[i] == 'u':
        if col_count > 0:
            col_count -= 1
    else:
        if col_count < n-1:
            col_count += 1
col_count += 1
row_count += 1
print(col_count, row_count)