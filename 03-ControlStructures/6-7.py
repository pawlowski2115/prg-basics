age = int(input('Enter your age:'))

if age < 13:
    print('child')
elif age >= 13 and age <= 19:
    print('teen')
elif age >= 20 and age <= 64:
    print('adult')
elif age >= 65:
    print('senior')