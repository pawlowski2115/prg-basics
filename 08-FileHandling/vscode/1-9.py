file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open('/Users/macbook/GitHub/prg-basics-1/08-FileHandling/vscode/it_company.csv', 'r') as f:
    number = 1
    for line in f:
        if job_title in line:
            print(f"{number}. {line.strip()}")
            number += 1