def f(sentence):
    words = sentence.split(" ")
    result = ""
    for i in words:
        result = result + str(i)
    return result

def g(sentence2):
    return sentence2.replace(" ","")

input(g("integrated development environment"))

