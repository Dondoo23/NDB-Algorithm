n = int(input())
count = 0

for hr in range(n+1):
    for mn in range(60):
        for sc in range(60):
            result = str(hr) + str(mn) + str(sc)
            if '3' in result:
                count += 1
print(count)