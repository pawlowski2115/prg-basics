###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_string = input('a=')
b_string = input('b=')
c_string = input('c=')
a = int(a_string)
b = int(b_string)
c = int(c_string)
volume = a * b * c
surface_area = (a * b * 2) + (b * c * 2) + (a * c * 2)
print(f'The voleme of a cube is {volume}')
print(f'The surface area of a cube is {surface_area}')