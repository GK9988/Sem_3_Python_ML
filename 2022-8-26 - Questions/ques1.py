print("Enter the following values: ")

intNum = int(input("Enter int value: "))
floatNum = float(input("Enter float value"))
str = input("Enter string: ")

arr = []

for i in range(5):
    tempInt = int(input("enter the numbers for the list: "))
    arr.append(tempInt)

strName = input("Enter name of the student: ")
strAge = int(input("Enter the age of the student: "))

dict1 = {
    "Name": strName,
    "Age": strAge,
}

mainTuple = (intNum, floatNum, str, arr, dict1)

print()
print(mainTuple)
print()

newTuple = mainTuple[::-1]

mainTuple = newTuple

print()
print("After reversing: ")
print()
print(mainTuple)
print()

print()
print(f"Index of list in the tuple is: {mainTuple.index(arr)}")
