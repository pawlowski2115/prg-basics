def f(name):
    word = name.split()
    result = ''
    for i in word:
        result = result + i[0]
    return result

print(f('Python'))
