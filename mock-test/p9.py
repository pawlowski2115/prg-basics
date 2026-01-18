def f(uid):
    copy ={}
    for name in uid:
        if not name in copy:
            copy[name] = 1
        elif name in copy:
            copy[name] += 1
    for i in copy.values():
        if i != 1:
            return False
        else:
            continue
    return True