number = int(input('Enter the number: '))
number_check = 0

if number == 0:
    number_check = '0'
elif number > 0:
    number_check = 'positive'
elif number < 0:
    number_check = 'negative'

print(f'The {number} is {number_check}')