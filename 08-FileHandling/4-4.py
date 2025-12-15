company = 'it_company.csv'


with open(company) as file:
    count = 0
    for line in file:               #petla pobiera kadą linię pojedynczo
     if count == 5:
         input("press the enter")
         count = 0
     else:
        print(line.strip())
        count += 1

    