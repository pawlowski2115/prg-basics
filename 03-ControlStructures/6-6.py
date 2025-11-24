parking_hour = int(input("Enter parking hour: "))
fee = 0

if parking_hour >= 1 and parking_hour <= 2:
    fee = 5
elif parking_hour >= 3 and parking_hour <= 6:
    fee = 15
elif parking_hour > 6:
    fee = 20

print(f"Parking fee for {parking_hour} hour(s) is: {fee}PLN")