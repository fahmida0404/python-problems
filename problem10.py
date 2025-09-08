# Program to calculate simple interest.

p = int(input("Enter Principle:"))
t = int(input("Enter time (years):"))
r = float(input("Enter rate of Interest (%):"))

interest = p*t*(r/100)

print("Simple Interest: ", interest)