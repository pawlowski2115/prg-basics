decimal = int(input('Enter a decimal number: '))
binary = bin(decimal)[2:] # remove '0b' prefix [2:]
print(f'Binary representation: {binary}')
hexadecimal = hex(decimal)[2:] # remove '0x' prefix [2:]
print(f'Hexadecimal representation: {hexadecimal}')