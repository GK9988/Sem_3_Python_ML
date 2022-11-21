import numpy as np

deg = int(input("Enter the degree of the polynomial: "))
coeffArr = np.array(())

print("Enter the values of the coefficient starting from highest degree")
for i in range(deg+1):
    x = int(input("Enter the Value: "))
    coeffArr = np.append(coeffArr, x)

roots = np.roots(coeffArr)

print(f"There are {roots.shape[0]} Roots: ")

for i in roots:
    print(f"\tRoot = {i}")
