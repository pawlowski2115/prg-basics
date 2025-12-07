products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

for product, quantity in products.items():
    print(f'Product: {product}, Quantity in stock: {quantity}')
total_quantity = 0
for quantity in products.values():
    total_quantity += quantity
print(f'Total quantity of all products in stock: {total_quantity}')