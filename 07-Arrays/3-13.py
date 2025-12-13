def occurs(number, array):
    for i in array:
        if i == number:
            return True
    return False

your_number = int(input("Enter a number: "))
print("Number:", your_number)
arr = [15, 38, 7, 23, 14]
print("Array: ", end=" ")
for j in arr:
    print(j, end=' ')
print()

if occurs(your_number, arr):
    print(f'Result: number {your_number} appears in the array')