###
# Calculation of circle area and circumference 
#
# determine radius and PI values
import math
print(math.pi)
radius = float(input('Enter circle radius in cm: '))
# calculate area 
area = math.pi * radius ** 2
# calculate circumference 
cirsumference = 2 * math.pi * radius
# print results
print(f'Circle area is (cm²): {area: .2f} and circumference (cm): {cirsumference: .2f}')