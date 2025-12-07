with open("/Users/macbook/GitHub/prg-basics-1/08-FileHandling/vscode/pets.txt", "r") as file:
    content = file.read()
    list_of_lines = content.splitlines(" ")
    print(len(list_of_lines))