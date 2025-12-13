arr = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]
       ] 

count = 0
row = 0
col =0 
for i in range(len(arr)):
    row = i + 1
    for j in range(len(arr[0])):
        col = j + 1
        arr[i][j] = row * col
        print(arr[i][j], end=" ")
    print()

