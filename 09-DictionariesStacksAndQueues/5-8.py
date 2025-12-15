# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
sum = 0 
for product in prices:
    if product in cart:
        cost = prices[product] * cart[product]
        sum = sum + cost
    else:
        continue

print(sum)

suma = 0
for product, quantity in cart.items():
    price = quantity * prices[product]
    suma = suma + price

print(suma)
