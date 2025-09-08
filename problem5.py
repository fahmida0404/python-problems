# Program to calculate the perimeter and area of a circle.

import math

r = int(input("Enter radius: "))

Pi=math.pi
per = 2*Pi*r
area = Pi*r*r

print("Perimeter of circle: ", per)
print("Area of circle: ", area)
