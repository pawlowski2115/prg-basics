arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

row = len(arr[0])
col = len(arr)
sum = 0
max_row = len(arr[0])-1

for i in range(col):
    for j in range(row):
        if j == max_row:
            sum = sum + arr[i][j]

print(sum)