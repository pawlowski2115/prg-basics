def rand_elem(array):
    import random
    element = random.choice(array)
    return element


tablica = [7,3,8,5,2,"pies",False]

print(rand_elem(tablica))