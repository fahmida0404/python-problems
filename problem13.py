# Program to program to convert specified days into years, weeks and the rest of the days.

while True:
    day = int(input("Enter total days:"))

    years = int(day/365)
    weeks = int((day%365)/7)
    days = (day%365)%7

    print("Years:", years)
    print("Weeks:", weeks)
    print("Days:", days)

    ans = input("Continue (y/n):")
    if not(ans=="y"):
        break