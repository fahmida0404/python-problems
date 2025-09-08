# Program to evaluate the ratio of (a+b) to (c-d), and print the result, if c-d is not equal to zero.

print("Enter four numbers: ")
a, b, c, d = map(int, input().split())

dividend = a+b
divisor = c-d

if divisor==0:
    print("Error! Divisor is zero.")
else:
    print(dividend/divisor)

