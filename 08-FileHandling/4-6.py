import re

def analyze_text():
    name = input("Enter a file name: ")
    try:
        with open(name, 'r', encoding='utf-8') as file:
            content = file.read()

        lines = content.splitlines()
        num_lines = len(lines)
        num_characters = len(content)
        words = re.findall(r'\b'+'\w+'+'\b', content.lower())
        num_words = len(words)
        print(f"Nazwa pliku: {name}")
        print(f"Liczba linii: {num_lines}")
        print(f"Liczba znaków: {num_characters}")
        print(f"Liczba słów: {num_words}")

    except FileNotFoundError:
        print("Your file does not exist")



analyze_text()