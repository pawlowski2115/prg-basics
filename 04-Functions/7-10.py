def f(x,y):
    result = 0
    for i in range(x,y+1):
        if i < 0:
            if i % 2 == 0:
                result = result + 1
            else:
                continue
        else:
            continue
    return result

print(f(-1,11))