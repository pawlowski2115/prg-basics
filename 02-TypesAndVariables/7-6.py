speed = int(input("Enter vehicle speed in km/h: "))
speed_valid = speed >= 40 and speed <= 140
print(f'Speed is valid: {speed_valid}')