import numpy as np
mt = []

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of colums: "))

for i in range(rows):
    arr = []
    for j in range(columns):
        val = int(input("Enter the Value: "))
        arr.append(val)
    mt.append(arr)

matrix = np.array(mt)

print("The user defined 2D array: ")
print(matrix)
