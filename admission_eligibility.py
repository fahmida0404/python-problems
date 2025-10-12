# Program to find the eligibility for admission to a professional course.

sub = ["Mathematics", "Physics", "Chemistry"]
marks = {}
sum1 = 0

for i in sub:
    m = float(input(f"Enter {i} marks:"))
    marks[i] = m #assigning marks to their respective subjects using dictionary
    sum1+=m

sum2 = marks["Mathematics"] + marks["Physics"]

if marks["Mathematics"]>=65 and marks["Physics"]>=55 and marks["Chemistry"]>=50:
    print("You are eligible for admission to the course.")
elif sum1>=180 or sum2>=140:
    print("You are eligible for admission to the course.")
else:
    print("You are not eligible for admission to the course.")
