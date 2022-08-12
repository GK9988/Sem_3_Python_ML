name = input("Enter the Student Name: ")
phy = int(input("Enter the marks in Physics: "))
eng = int(input("Enter the marks in English: "))
cs = int(input("Enter the marks in Computer Science: "))
chem = int(input("Enter the marks in Chemistry: "))
maths = int(input("Enter the marks in Maths: "))

print()
print()
print(f"****** Result of the student {name} *******")
perc = (phy + maths + chem + cs + eng) / 5
if(perc <= 100 and perc > 90):
    grade = "A"

elif(perc <= 90 and perc > 80):
    grade = "B"

elif(perc <= 80 and perc > 70):
    grade = "C"

elif(perc <= 70 and perc > 60):
    grade = "D"

elif(perc <= 60):
    grade = "E"

print(f"Percentage of the Student: {perc}%")
print("Grade of the student: ", grade)
