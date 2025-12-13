array1 = ["water", "book", "sky"]
array2 = ["water", "book", "sky"]

def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

def compare2(arr1, arr2):       #prosta wersja
    return arr1 == arr2

w = [True,False]   
k = [True,False,True]
a = [5,3,1]   
b= [5,3,1]
u = [3,2,1]   
y = [3,2]

print(compare(array1, array2))
print(compare(w, k))
print(compare(a, b))
print(compare(u, y))