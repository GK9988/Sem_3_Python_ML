marks = int(input("Enter the marks: "))

print()

if marks > 85 and marks <= 100:
    print("Excellent")
elif marks > 75 and marks <= 85:
    print("Good")
elif marks > 60 and marks <= 75:
    print("Average")
elif marks > 45 and marks <= 60:
    print("Work Hard")
else:
    print("Fail")
