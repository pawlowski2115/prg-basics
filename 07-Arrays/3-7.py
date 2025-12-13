name = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

lenght = len(name)
suma = [0] * lenght

for i in range(lenght):
    for j in range(len(name[i])):
        suma[i] += 1

max_word =  suma[0]
max_name = name[0]

for j in range(len(suma)):          #system dobpasowywania największej waftości do jej definicji
    if suma[j] > max_word:
        max_word = suma[j]
        max_name = name[j]

print(f'The longest name is {max_name}')
print(f'Length of the longest name is {max_word}')