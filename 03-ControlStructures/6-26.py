i = 0
pin = str("0805")

while i < 3:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print("PIN accepted.")
        break   
    else:
        print("Incorrect...")
        i += 1
else:
    print("Sorry, your payment card has been blocked.")

print("Thank you for using our ATM.")