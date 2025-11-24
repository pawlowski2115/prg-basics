number = int(input("Enter a number of products purchased: "))
price = int(input("enter the price: "))
total_price = 0
 
if number > 2:
    total_price = 2 * price + (number - 2) * price * 0.75
else:
    total_price = number * price

print(f'Number of products purchased: {number}')
print(f'Product price: {price}')
print(f'Amount to pay: {total_price}')