def f(d):
    result = 0
    avg = sum(d.values()) / len(d)
    for i in d.values():
        if i > avg:
            result += 1
    return result
    