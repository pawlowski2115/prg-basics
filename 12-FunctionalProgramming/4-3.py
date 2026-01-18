grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2.0]
new = list(filter(lambda x: x>2.0, grades))
avg = sum(new)/len(new)
print(f"{avg:.2f}")