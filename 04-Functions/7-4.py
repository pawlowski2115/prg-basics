def check(sentence, letter):
    count = 0
    for char in sentence:
        if char == letter:
            count = count + 1
    return count

zdanie = "ela ma kota"
print(check(zdanie, 'a'))
