def check(number,x,y):
    if number >= x and number <= y:
        return True
    else:
        return False


if check(7,6,15):
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")

