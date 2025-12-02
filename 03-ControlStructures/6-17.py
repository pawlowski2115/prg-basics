time = input('Enter time (24-hour format): ')
hour = time.split(':')[0]
min = time.split(':')[1]
hour = int(hour)
min = int(min)
if hour < 12:
    dn = 'am'
elif hour >= 12:
    dn = 'pm'
    hour = hour - 12

print(f'Time in 12-hour format: {hour:02d}:{min:02d}{dn}')
