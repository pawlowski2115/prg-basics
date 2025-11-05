price = float(input("Enter the price of the item: "))
discount = float(input("Enter the discount percentage: "))
price_after_discount = price * (1 - discount / 100)
reduction = price - price_after_discount
print(f'Enter price: {price: .2f}')
print(f'Enter discount: {discount: .2f}%')
print(f'Price with discount: {price_after_discount: .2f}')
print(f'Reduction: {reduction: .2f}')