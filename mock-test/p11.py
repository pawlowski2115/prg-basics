
def f(car,order):
    if order == 1:
        return sorted(car, key=lambda dictionary: list(dictionary.keys())[0])
    elif order == 2:
        return sorted(car, key=lambda dictionary: list(dictionary.values())[0], reverse=True)


