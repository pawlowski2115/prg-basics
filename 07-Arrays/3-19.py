arr = [10.5, 3.2, 18.0, 7.1, 25.5, 1.9, 14.7]

number = float(input("Enter a number: "))
count = 0

for i in arr:
    if i > number:
        count += 1
        print(i)

print(f'Ilosc liczb w tablicy wiekszych od {number} wynosi: {count}')