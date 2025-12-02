amount = int(input("Enter amount: "))

five = amount // 5
amount = amount % 5
two = amount // 2
amount = amount % 2
one = amount // 1

print(f'The amount of PLN {amount} in coins: ')
print(f'5 PLN coins: {five}')
print(f'2 PLN coins: {two}')
print(f'1 PLN coins: {one}')