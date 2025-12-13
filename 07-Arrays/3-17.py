krotka = (50,20,40,50,30,50)
value = 50

number = krotka.count(value)                    #metoda count
print(f'Number of occurrences: {number}')

number2 = 0
for i in krotka:                                #pętla
    if i == value:
        number2 += 1

print(f'Number of occurrences (loop): {number2}')