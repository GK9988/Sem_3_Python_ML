phy = int(input("Enter the marks of Physics: "))
chem = int(input("Enter the marks of Chemistry: "))
maths = int(input("Enter the marks of Maths: "))

avg = (phy + chem + maths) / 3
print()
print()

if(avg >= 98):
    print("Student is Eligible for Scholarship")
else:
    print("Student is NOT Eligible for Scholarship")

print(f"Percentage Scored: {round(avg, 2)}")
