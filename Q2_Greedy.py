arr = input()
number = []
for i in arr:
    number.append(int(i))

result = 0
first = number.pop(0)
while number:
    second = number.pop(0)
    if first == 0 or second == 0:
        result = first + second
    else:
        result = first * second
    first = result

print(result)