def f(fnc,res):
    new_arr = list(filter(fnc,res))
    return max(new_arr) - min(new_arr)