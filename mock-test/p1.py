def f(word):
    l = len(word)
    arr = []
    for i in range(l): 
        result = ""
        for j in range(l):
            if i == j:
                result += word[j].upper()
            else:
                result += word[j].lower()
        arr.append(result)           
    return "-".join(arr)
