# Program to calculate the total, average, and percentage of marks of five subjects.

print("Enter marks of five subjects:")

total = 0 

for i in range(1,6,1):
    mark = float(input())
    total+=mark
    
average = total/5
percentage = (total/500)*100 #same as average as total mark of each subject is 100

print("Total marks:", total)
print("Average:", average)
print("Percentage:", percentage, "%")
