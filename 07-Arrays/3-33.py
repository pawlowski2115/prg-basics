arr = [
    [1,2,3,4,5],
    [6,4,8,9,2],
    [0,8,3,6,1]
]

first_column = 0
last_column = len(arr[0])-1

print("Before changes:")
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

print("After changes:")

for row in arr:
    row[first_column], row[last_column] = row[last_column], row[first_column]       #zamiana kolumn!

for i in arr:
    for j in i:
        print(j, end=" ")
    print()