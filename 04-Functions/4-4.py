###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)
    number = str(number)
    result = 0
    for char in number:
        char = int(char)
        result = result + char
    return result

print(sum_digits(12345))  # Output: 15
print(sum_digits(-678))   # Output: 21