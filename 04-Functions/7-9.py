def f(number,even):
    suma = 0
    for char in str(number):
        if even is True:
            if int(char) % 2 == 0:
                suma = suma + int(char)
            else:
                continue
        elif even is False:
            if int(char) % 2 != 0:
                suma = suma + int(char)
    return suma

print(f(13115,True))