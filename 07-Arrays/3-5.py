arr = [15, 8, 31, 47, 2, 19]

print("Original array:", arr)

len = len(arr)
sum = 0
for i in range(len):
    sum += arr[i]

print("Sum of elements:", sum)
average = sum / len
print(f'Average of elements: {average:.2f}')