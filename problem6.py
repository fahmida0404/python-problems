# Program to find the third angle of a triangle if two angles are given.


a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))

c = 180-(a+b)  

print("Third angle: ", c)