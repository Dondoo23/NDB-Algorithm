n = int(input())

std = list()
for i in range(n):
    input_data = input().split()
    std.append((input_data[0], int(input_data[1])))

def setting(data):
    return data[1]

students = sorted(std, key=setting)
for student in students:
    print(student[0],end=' ')