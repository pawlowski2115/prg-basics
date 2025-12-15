import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

#tworzenie nowego stosu
stack = queue.LifoQueue()

#dodawanie nowych elementów
liczby_do_dodania = [2,3,7,4,1,9,8]     #dodanie liczb za pomocą pętli
for num in liczby_do_dodania:
    stack.put(num)
    print("dodano", num)

sum_last_two = 0
count = 0
while count < 2:                    #sumowanie dwóch ostatnich wartości
    num = stack.get()
    sum_last_two = sum_last_two + num
    count +=1

print(sum_last_two)

sum_rest = 0
while not stack.empty():            #sumowanie reszty wartości w stosie
    number = stack.get()
    sum_rest = sum_rest + number

print(sum_rest)
"""
Note the order of the printed elements.
The last added element is printed first.
"""
