def f(n):
    result = ""
    for i in range(n):
        result = result + "*" 
        if i < n-1:
            result = result + "/"
    return result

print(f(1))