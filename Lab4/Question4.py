import numpy as np

arr = np.array([10, 21, 32, 43, 54, 65])
a = 0

arr = arr - 5
print(arr)

for i in arr:
    if i > 40:
        a += 1
print("The amount of numbers that bigger than 40 are: " + str(a))

print("This is a 2X3 array: ")
x = arr.reshape(2, 3)
print(x)

print("This is a 3x2 array: ")
y = arr.reshape(3, 2)
print(y)
