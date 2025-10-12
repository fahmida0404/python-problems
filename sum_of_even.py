# Program to program to find the sum of all even numbers between 1 to n.

n = int(input("Enter a number greater than 1:"))

sum = 0

for i in range(1,n+1):
    if i%2==0:
        sum+=i

print(f"Sum of all even numbers from 1 to {n} is {sum}.")