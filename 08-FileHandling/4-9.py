import csv

name = 'it_company.csv'
with open(name, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Job Title']=="Graphic Designer":
            first_name = row['First Name']
            last_name = row['Last Name']
            email = row['Email']
            print(first_name, last_name, email)