arr = [7,9,2,4,5,6]
print(arr)
even = []
odd = []
for i in arr:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)

arr = even + odd
print(arr)