first = [2, 5, 6, 8]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]



for i in first:
    if not i in second:
        print("The first array is NOT a subset of the second one")
        break
    else:
        continue
else: 
    print("The first array is a subset of the second one")

