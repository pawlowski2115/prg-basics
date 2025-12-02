def f(binary):
    for char in binary:
        if char == "0" or char == "1":
            continue
        else:
            return False
    else:
        return True

print(f("101a0"))