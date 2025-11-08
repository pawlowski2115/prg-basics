from math import pi
circumference = float(input('Enter tree circumference in cm: '))
diameter = circumference / pi
can_cut = diameter >= 50
print(f'Tree can be cut down: {can_cut}')