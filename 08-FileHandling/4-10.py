import csv

with open('clothing.csv','r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        price = float(line['Price'])
        quantity = int(line['Stock_Quantity'])
        if price < 60 and quantity < 40:
            print(f"Produkt: {line['Product_Name']}, Cena: {price:.2f}, Stan: {quantity}")