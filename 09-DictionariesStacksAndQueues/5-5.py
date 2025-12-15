paragraph = "cat dog mouse cat rat cat mouse"

words = paragraph.split()
dictionary ={

}

for i in words:
    if i not in dictionary:
        dictionary[i] = 1
    elif i in dictionary:
        dictionary[i] += 1

print("Liczba wystąpień słów w zdaniu: ", dictionary)