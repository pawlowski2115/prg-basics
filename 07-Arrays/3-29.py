def create_2d_arr(x,y):
    arr = []
    for i in range(x):
        arr.append([])          #dodajemy pustą tablicę
        for j in range(y):          
            arr[i].insert(j,0)      #wstawiamy do wiersza nr.0,1,2...itd wartosć -> .insert(indeks, wartość)
    return arr


print(create_2d_arr(3,5))