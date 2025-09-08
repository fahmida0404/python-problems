# Program to check whether you are eligible to make a NID Card or not.

n = int(input("Enter your age: "))

if n<0:
    print("Invalid number.")
elif n>=18:
    print("You are eligible to make a NID Card.")
else:
    print("You are not eligible to make a NID Card.")