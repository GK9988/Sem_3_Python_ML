a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print()
print("****** Operator Menu ******")
print('''
    1. Add
    2. Subtract.
    3. Normal Division
    4. Floor Division
    5. Modulo
    6. Multiplication
    7. Comparison
    8. Bitwise AND
    9. Bitwise OR
    10. Bitwise NOT
    11. Bitwise XOR

    Press -1 for exit
''')
print()

choice = 0

while(choice != -1):
    print()
    choice = int(input("Enter your Choice: "))
    if(choice == 1):
        print(f"Addition of these numbers is: {a + b}")
    elif(choice == 2):
        print(f"Subtraction of these numbers is: {a - b}")
    elif(choice == 3):
        print(f"Normal Division of these numbers is: {a / b}")
    elif(choice == 4):
        print(f"Floor Division of these numbers is: {a // b}")
    elif(choice == 5):
        print(f"Modulo of these numbers is: {a % b}")
    elif(choice == 6):
        print(f"Multiplication of these numbers is: {a * b}")
    elif(choice == 7):
        if(a > b):
            print("Number 1 is greater")
        elif (a < b):
            print("Number 2 is greater")
        else:
            print("Both numbers are equal")
    elif(choice == 8):
        print(f"Bitwise And of these numbers: {a&b}")
    elif(choice == 9):
        print(f"Bitwise And of these numbers: {a|b}")
    elif(choice == 10):
        print(f"Bitwise And of first numbers: {~a}")
        print(f"Bitwise And of second numbers: {~b}")
    elif(choice == 11):
        print(f"Bitwise And of these numbers: {a^b}")
