import re

name = "files.txt"
with open(name, 'r', encoding='utf-8') as file:
    pattern = r'^\w+\.\w{4}$'
    for line in file:
        if re.search(pattern, line.strip()):
            print(line.strip())
        else:
            continue

