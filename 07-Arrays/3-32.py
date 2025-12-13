arr = [
    [1,2,3,4,5],
    [6,4,8,9,2],
    [0,8,3,6,1]
]

first_row = 0
last_row = len(arr) - 1

print("Before changes:")
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

print("After changes:")

arr[first_row], arr[last_row] = arr[last_row], arr[first_row]     #zamiana wierszy!

for i in arr:
    for j in i:
        print(j, end=" ")
    print()