# Program to check whether the year is a leap year or not.

while True:
    a = int(input("Enter a year: "))
    if a%400==0:
        print(f"{a} is a leap year.")
    elif a%4==0 and a%100!=0:
        print(f"{a} is a leap year.")
    else:
        print(f"{a} is not a leap year.")
        
    ans = input("Continue (y/n):")
    if not(ans=="y"):
        break