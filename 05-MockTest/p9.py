def f(sentence):
    count = 0
    for letter in sentence:
        if letter in {"a", "e", "i", "o", "u", "y"}:
            count += 1
    return count
