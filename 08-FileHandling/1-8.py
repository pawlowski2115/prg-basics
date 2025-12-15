def read_file(text):
    with open(text) as file:
        content = file.read()
    return content

animal_file = read_file('pets.txt')
print(animal_file)

animal_array = animal_file.split()
print("Number of words in text: ", len(animal_array))