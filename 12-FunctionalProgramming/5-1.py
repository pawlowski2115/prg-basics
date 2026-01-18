from functools import reduce

# Function to add two numbers
suma = lambda x, y: x+y

numbers = [1, 2, 3, 4, 5]

# Using reduce to sum the numbers
result = reduce(suma, numbers)
print(result)  