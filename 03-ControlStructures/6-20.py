decimal = int(input("Enter a decimal number: "))
binary = ''
while decimal != 0:
    binary = binary + str(decimal % 2)
    decimal = decimal // 2
print(binary[::-1])


