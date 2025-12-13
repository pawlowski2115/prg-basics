#Wyszukiwanie największej i najmniejszej wartości w tablicy 2D



arr = [
        [-38, 19], 
        [5,40],
        [-7,11],
        [29,16]
       ]

max_num = arr[0][0]
max_row = 0
max_col = 0
min_num = arr[0][0]
min_row = 0
min_col = 0

for i in range(len(arr)):
   for j in range(len(arr[0])):
        current = arr[i][j]
        if current > max_num:
            max_num = current
            max_row = i
            max_col = j
        if current < min_num:
            min_num = current
            min_row = i
            min_col = j

print(f'Max value is {max_num} in arr[{max_row}][{max_col}]')
print(f'Min value is {min_num} in arr[{min_row}][{min_col}]')


