# Program to finds out the grade using a switch case.

marks = float(input("Enter your marks:"))

grades = {
    range(0, 60): "F",
    range(60, 65): "D",
    range(65, 70): "D+",
    range(70, 74): "C-",
    range(74, 77): "C",
    range(77, 80): "C+",
    range(80, 84): "B-",
    range(84, 87): "B",
    range(87, 90): "B+",
    range(90, 101): "A+",
}

for key in grades.keys():
    if marks in key:
        grade = grades[key]
    else:
        grade = "Error"
        
match grade:
    case "A+":
        print("You have got A+")
    case "B+":
        print("You have got B+")
    case "B":
        print("You have got B")
    case "B-":
        print("You have got B-")
    case "C+":
        print("You have got C+")
    case "C":
        print("You have got C")
    case "C-":
        print("You have got C-")
    case "D+":
        print("You have got D+")
    case "D":
        print("You have got D")
    case "F":
        print("You have got F")
    case "Error":
        print("Invalid Marks.")