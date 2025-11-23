###
# Calculates the sum of integer numbers in the range <1,5>
#
sum = 0
sum2 = 0

for i in range(5,11):
    sum += i
    sum2 = sum2 + i

print(f'Sum is {sum} {sum2}')