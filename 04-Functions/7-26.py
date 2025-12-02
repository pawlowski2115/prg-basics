def f(text):
    result =''
    for i in range(len(text)):
        result = result + text[i]
        if i < len(text) - 1:
            result = result + '-'
    return result
print(f("ue"))