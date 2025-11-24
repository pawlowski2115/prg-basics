dog_age = int(input("Enter a dog's age: "))
human_age = 0

if dog_age > 2:
    dog_age = dog_age - 2
    human_age = 2 * 10.5 + dog_age * 4
elif dog_age <= 2:
    human_age = dog_age * 10.5

print(f"The dog's age in dog's years is {human_age} years.")