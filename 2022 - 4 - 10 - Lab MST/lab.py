sub1 = int(input("Enter Marks of Subject 1: "))
sub2 = int(input("Enter Marks of Subject 2: "))
sub3 = int(input("Enter Marks of Subject 3: "))
sub4 = int(input("Enter Marks of Subject 4: "))
sub5 = int(input("Enter Marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5

perc = (total / 5)

if(perc <= 100 and perc > 90):
    grade = "A"
elif(perc <= 90 and perc > 80):
    grade = "B"
elif(perc <= 80 and perc > 70):
    grade = "C"
elif(perc <= 70 and perc > 55):
    grade = "D"
elif(perc < 55):
    grade = "E"
else:
    print("Marks Entered are not correct")

print(f"Percentage Marks Scored: {perc}")
print(f"Grade Obtained: {grade}")
