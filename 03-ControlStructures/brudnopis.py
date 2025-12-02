def f(number,even):
    result = 0
    number = str(number)
    if even is True:
        for i in number:
            if int(i) % 2 == 0:
                result = result +int(i)
            else:
                continue
    elif even is False:
        for i in number:
            if int(i) % 2 != 0:
                result = result +int(i)
            else:
                continue
    return result

print(f(3124,False))

