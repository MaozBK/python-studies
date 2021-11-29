num = int(input("Please enter 4 digit number: "))
if len(str(num)) != 4:
    print("Invalid number!")
else:
    num1 = num % 10
    num2 = (num // 10) % 10
    num3 = (num // 100) % 10
    num4 = (num // 1000) % 10
    if num1 < num2 and num2 < num3 and num3 < num4:
        print("Decreasing Order")
    else:
        print("Not Decreasing Order")


