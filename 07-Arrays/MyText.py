
def number_of_words(variable):      #podzial na pojedyncze słowa do tablicy
    words = variable.split(" ")
    return len(words)

def ordered_list(variable):                 #sortowanie tablicy: atrybuty key i reverse
    words = variable.split()
    sorted_words = sorted(words, key=len, reverse=True)
    return sorted_words

def alfabetical(variable):
    words = variable.split()
    sorted_words = sorted(words, key=str.lower)     #zmiana na małe litery!
    return sorted_words