# Program to display a suitable weather message according to the temperature.

t = float(input("Enter temperature in Centrigrade:"))

if t<0:
    print("Freezing weather.")
elif 0<=t<10:
    print("Very cold weather.")
elif 10<=t<20:
    print("Cold weather.")
elif 20<=t<30:
    print("Normal.")
elif 30<=t<40:
    print("It’s hot.")
else:
    print("It’s very hot.")
