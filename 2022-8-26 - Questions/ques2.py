arr = []

for i in range(3):
    newInt = int(input("enter values for the list: "))
    arr.append(newInt)

newValue = int(
    input("Enter the number you want to insert into the list at second position: "))

print()
print("list before insertion: ")
print()
for i in arr:
    print(i, end=' ')


arr.insert(2, newValue)

print()
print("list after insertion: ")
print()
for i in arr:
    print(i, end=' ')
