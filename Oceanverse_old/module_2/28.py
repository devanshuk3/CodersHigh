marks = int(input("Enter your marks:"))
grade=""
if marks>=90:
    grade = 'A'
if marks >= 80 and marks < 90:
    grade = 'B'
if marks >= 70 and marks < 80:
    grade = 'C'
if marks >= 60 and marks < 70:
    grade = 'B'
if marks<70:
    grade = 'F'
print("The grade is: ",grade)

