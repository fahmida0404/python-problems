# Program to calculate compound interest.

p = int(input("Enter Principle:"))
t = int(input("Enter time (years):"))
r = float(input("Enter rate of Interest (%):"))

interest = p*(pow(1+(r/100),t))-p 

print("Compound Interest: ", interest)