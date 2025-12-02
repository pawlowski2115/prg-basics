def time_string(hours, minutes, time_format):
    if time_format == '12':
        if hours >= 12:
            time_format = 'pm'
        elif hours < 12:
            time_format = 'am'
    elif time_format == '24':
        time_format = ' '
    time = str(hours) + ":" + str(minutes) + time_format
    return time

print(time_string(10, 30, '12'))  # Output: "10:30 AM"