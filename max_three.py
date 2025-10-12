# Program to to find the maximum between three numbers.

print("Enter three unique numbers: ")

a, b, c = map(int, input().split())

if a>b and a>c:
    print("Max: ", a)
elif b>a and b>c:
    print("Max: ", b)
else:
    print("Max: ", c)