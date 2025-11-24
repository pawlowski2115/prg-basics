current_price = 140.00
previous_price = 200.00

print(f'Current product price: {current_price: .2f} PLN')
print(f'Previous product price: {previous_price: .2f} PLN')

difference = previous_price - current_price
discount_percentage = (difference / previous_price) * 100

if discount_percentage >= 10:
    print("Buy the product!!")
    print(f'Product price reduced by {discount_percentage: .2f} %')