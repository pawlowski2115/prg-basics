def f(password):
    if len(password) < 6:
        return False
    for i in password:
        if password.count(i) > 1:
            return False
    else:
        return True
    
print(f(''))