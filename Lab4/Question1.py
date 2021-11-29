gcd = 0
a = int(input("Please Enter the first number: "))
b = int(input("Please enter the second number: "))

if a > b:
    smallNum = b
else:
    smallNum = a

for j in range(1, smallNum + 1):
    if a % j == 0 and b % j == 0:
        gcd = j
print("The gcd between", str(a), " and ", str(b), " is ", str(gcd))
