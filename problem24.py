# Program to check whether a triangle is valid or not.

print("Enter three angles of a traingle:")
a, b, c = map(int, input().split())

if a==0 or b==0 or c==0:
    print("The triangle is not valid.")
elif (a+b+c)==180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")