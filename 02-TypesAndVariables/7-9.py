import random
dice_roll = random.randint(1,6)
print(f'Dice rolled: {dice_roll}')
special_number =dice_roll == 6 or dice_roll == 1
print(f'Special number rolled: {special_number}')