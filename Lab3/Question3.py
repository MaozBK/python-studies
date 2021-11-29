x = int(input("Enter the first number: "))
op = str(input("Enter operation required: "))
y = int(input("Enter second number: "))

if op == '+':
    print("Result of x + y is: ", (x + y), " Operation is '+'")
elif op == '-':
    print("Result of x - y is: ", (x - y), " Operation is '-'")
elif op == '*':
    print("Result of x * y is: ", (x * y), " Operation is '*'")
elif op == '/':
    print("Result of x / y is: ", (x / y), " Operation is '/'")
elif op == '%':
    print("Result of x % y is: ", (x % y), " Operation is '%'")
elif op == '**':
    print("Result of x ** y is: ", (x ** y), " Operation is '**'")
elif op == '//':
    print("Result of x // y is: ", (x // y), " Operation is '//'")
else:
    print("Invalid Operation has taken place")
