countries = [
{"name":"Poland", "population":38000000},
{"name":"Norway", "population":38000000},
{"name":"Russia", "population":38000000},
{"name":"China", "population":38000000},
{"name":"Greece", "population":38000000}
]

print("COUNTRY         POPULATION")
for i in countries:
    for data in i.values():
        print(f'{data:12}', end="")
    print()