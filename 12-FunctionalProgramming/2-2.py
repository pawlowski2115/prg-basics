names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']


sorted_names = sorted(names, key = lambda name: len(name), reverse= True)
print(sorted_names)