# Program to to check whether a number is negative, positive, or zero.

n = int(input("Enter any number: "))

if n==0:
    print(f"{n} is zero.")
elif n>0:
    print(f"{n} is positive.")
else:
    print(f"{n} is negative.")