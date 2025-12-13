table = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
count = 0
for i in range(len(table)):
    for j in range(len(table[i])):
        if j == count:
            table[i][j] = 1
        print(table[j][i], end=' ')
    count += 1
    print()
