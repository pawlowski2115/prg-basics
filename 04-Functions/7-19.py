def f(number):
    number = str(number)
    result = 0
    for i in number:
        count = number.count(i)
        if count > 1:
            result = result + int(i)
    return result

print(f(513553007))