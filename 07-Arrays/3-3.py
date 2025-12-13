array = [8, 2, 5, 1, 9]

print(array)

for i in range(len(array)):             #zmiana wartosci w tablicy
    array[i] = array[i] * array[i]

print(array)

new_array = [0] * len(array)
count = 0
for i in array:                     #tworzenie nowej tablicy
    new_array[count] = i * i
    count += 1


print(new_array)