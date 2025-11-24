jacket = 40
underwear = 70 
shoes = 20

total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n) ')
extra_spin = input('Extra spin? (y/n) ')

if program == "j":
    total_washing_time =+ jacket
    if extra_rinse == "y":
        total_washing_time =+ 15
    if extra_spin == "y":
        total_washing_time =+ 9
elif program == "u":
    total_washing_time =+ underwear
    
elif program == "s":
    total_washing_time =+ shoes

else:
    print("Something went wrong!")

print(f'Total washing time: {total_washing_time} minutes')