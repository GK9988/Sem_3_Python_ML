n = int(input('Enter the number of elements you want in the list: '))
arr = []

for i in range(n):
    a = int(input(f"Enter Number {i+1}: "))
    arr.append(a)

print("\nThe list is: ")

for i in range(n):
    print(arr[i], end=" ")

arr.reverse()

print('\nreversed list: ')

for i in range(n):
    print(arr[i], end=" ")