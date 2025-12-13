Tuple = (10,20,30,40,50)
print("Tuple: ", end=" ")
for i in Tuple:
    print(i, end=" ")
print()


print("Reverse order: ", end=" ")       
lenght = len(Tuple)
for i in range(lenght -1, -1, -1):
    print(Tuple[i], end=" ")
print()


print("Reverse order: ", end=" ")       # using reversed()
for i in reversed(Tuple):
    print(i, end=" ")
print()