# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for i in range(len(seats)):
      for j in range(len(seats[i])):
         total += 1
   return total

def seats_available(seats):
   available = 0
   for i in range(len(seats)):
      for j in range(len(seats[i])):
         if seats[i][j] == 'A':
            available += 1
   return available

def seats_booked(seats):
   booked = 0
   for i in range(len(seats)):
      for j in range(len(seats[i])):
         if seats[i][j] == 'B':
            booked += 1
   return booked

def seat_status(seats, row, place):
    check = " "
    if seats[row-1][place-1] == 'A':
        check = 'available'
    elif seats[row-1][place-1] == 'B':
        check = 'booked'
    return check

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))