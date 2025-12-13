def sec_largest(arr):
    first = 0
    second = 0
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    return second


def difference(arr):
    max_value = arr[0]
    min_value = arr[0]
    lenght = len(arr)

    for i in range(lenght):
        if arr[i] > max_value:
            max_value = arr[i]
        if arr[i] < min_value:
            min_value = arr[i]
    return max_value - min_value

def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        mid1 = len(arr)/2 -1
        mid2 = len(arr)/2
        return (arr[mid1] + arr[mid2]) /2
    else:
        mid = len(arr) //2
        return arr[mid]
    
def two_element(arr):
    new_arr = []
    max_value = max(arr)
    min_value = min(arr)
    new_arr = [min_value, max_value]
    return new_arr

def string(arr):
    module = ""
    for i in arr:
        module = module + str(i) + "-"
    return module[:-1]
