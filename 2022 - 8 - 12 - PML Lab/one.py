a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print()
print()
print("****** Calculation Menu ******")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print()
print()

choice = int(input("Enter your choice: "))

if(choice == 1):
    print(f"Addition of the Numbers: {a+b}")
elif(choice == 2):
    print(f"Subtraction of the Numbers: {a-b}")
elif(choice == 3):
    print(f"Multiplication of the Numbers: {a*b}")
elif(choice == 4):
    print(f"Division of the Numbers: {a/b}")
else:
    print("Enter valid choice")

