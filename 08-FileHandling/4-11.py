

output_lines = []
for num in range(1,101):
    power_2 = num ** 2
    power_3 = num ** 3
    line = f"{num},{power_2},{power_3}"
    output_lines.append(line)




with open('number.txt','w') as file:
    file.write('\n'.join(output_lines))