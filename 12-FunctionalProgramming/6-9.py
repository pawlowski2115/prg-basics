temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

positive = list(filter(lambda x: x[1]>0, temp.items()))

cities = list(map(lambda x: x[0], positive))

print(" ".join(cities))