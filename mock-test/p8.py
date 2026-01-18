prods = ["water","cheese","tomato"]
fnc1 = lambda x: "id:"+x[:2] 
fnc2 = lambda x: (x[0]+x[-1]).upper()

def f(fnc,prods):
    return list(map(fnc,prods))

print(f(fnc1,prods))
print(f(fnc2,prods))