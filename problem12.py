# Program to convert minutes to hours and minutes.

while True:
    min = int(input("Enter total minutes:"))

    hours = int(min/60)
    mins = min%60

    if hours>1 and mins>1:
        print(f"{hours} hours and {mins} minutes")
    elif hours>1 and not(mins>1):
        print(f"{hours} hours and {mins} minute")
    elif not(hours>1) and mins>1:
        print(f"{hours} hour and {mins} minutes")
    else:
        print(f"{hours} hour and {mins} minute")

    ans = input("Continue (y/n):")
    if not(ans=="y"):
        break