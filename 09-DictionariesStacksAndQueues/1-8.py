price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("Price before discount:")
for item, price in price_list.items():
    print(f'{item}: {price}')
total_price = sum(price_list.values())
print(f'Total price: {total_price}')

discount = 0.1

for item, price in price_list.items():
    print(f'{item}: {price * (1 - discount):.2f}')