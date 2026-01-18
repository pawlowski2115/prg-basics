temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

positive = dict(filter(lambda x: x[1] >0, temp.items()))

city = list(map(lambda x: x, positive.keys()))

print(", ".join(city))



test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]


condition = list(filter(lambda x: x["result"] > 50 and x["result"] < 70, test_results))

results = list(map(lambda x: x["name"], condition))
print(", ".join(results))