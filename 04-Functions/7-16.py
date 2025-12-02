def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for i in range(3,n+1):
        temp_b = b
        b = a + b 
        a = temp_b
    return b

print(f(7))