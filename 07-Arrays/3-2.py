number = [ 15, 8, 31, 47, 2, 19 ]

print(number[::-1])
d = len(number)

for i in range(d//2):
    number[i], number[d-1-i] = number[d-1-i], number[i]

print(number)
