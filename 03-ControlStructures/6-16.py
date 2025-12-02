jacket = 40
underwear = 70 
shoes = 20
rinse = 15
spin = 9

total_washing_time = 0

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n) ')
extra_spin = input('Extra spin? (y/n) ')

if program == "j":
    total_washing_time =+ jacket
    if extra_rinse == "y":
        total_washing_time = total_washing_time + rinse
    if extra_spin == "y":
        total_washing_time =+ spin
elif program == "u":
    total_washing_time = total_washing_time + underwear
    if extra_rinse == "y":
        total_washing_time = total_washing_time + rinse
    if extra_spin == "y":
        total_washing_time =+ spin
elif program == "s":
    total_washing_time = total_washing_time + shoes
    if extra_rinse == "y":
        total_washing_time = total_washing_time + rinse
    if extra_spin == "y":
        total_washing_time =+ spin
else:
    print("Something went wrong!")

print(f'Total washing time: {total_washing_time} minutes')

