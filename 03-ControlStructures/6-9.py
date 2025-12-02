name = input("Enter your name: ")

if name.endswith("a"): 
    print(f'{name}-- Polish female name')

lenght = len(name) - 1
last_char = name[lenght]

if last_char == "a":
    print(f'{name}-- Polish female name')
