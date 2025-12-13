name = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

lenght = len(name)
suma = [0] * lenght


max_name = max(name, key=len)
max_word = len(max_name)

print(f'The longest name is {max_name}')        
print(f'Length of the longest name is {max_word}')