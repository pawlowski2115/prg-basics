def avg_speed(distance,hours,minutes):
    time = hours + (minutes/60)
    avg = distance / time
    return avg

dist = float(input("Enter distance in km: "))
h = int(input("Enter number of travel hours: "))
m = int(input("Enter number of travel minutes: "))

print(f"Average speed: {avg_speed(dist,h,m):.1f} km/h")