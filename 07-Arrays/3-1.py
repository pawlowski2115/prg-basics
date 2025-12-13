number = [34,7,19,4,21,8]

number_len = len(number)

count = 0
sum = 0

while count < number_len:
    if number[count] % 2 ==  0:
        sum += number[count]
    count += 1

print(sum)