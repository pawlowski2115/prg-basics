values = [2, 5, 1, 6]

n = len(values)
for i in range(n):
    print(i)
    for j in range(n - i - 1):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]



print(values)