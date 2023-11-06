n = input()
num = []
for i in n:
    num.append(int(i))
count1 = 0
count0 = 0
if num[0] == 0:
    count0 += 1
else:
    count1 += 1
start = num[0]
for i in range(1, len(num)):
    if num[i] == 1:
        if num[i-1] == 0:
            count1 += 1
    else:
        if num[i-1] == 1:
            count0 += 1

print(min(count0, count1))