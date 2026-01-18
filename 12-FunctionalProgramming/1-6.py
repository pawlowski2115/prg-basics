avg_speed = lambda distance,hours,minutes: distance / (hours + (minutes/60))

dist = float(input("Enter distance in km: "))
h = int(input("Enter number of travel hours: "))
m = int(input("Enter number of travel minutes: "))

print(f"Average speed: {avg_speed(dist,h,m):.1f} km/h")