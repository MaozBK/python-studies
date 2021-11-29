grade = int(input("Please enter your grade: "))
if grade >= 0 and grade < 60:
    print("Fail")
elif grade >= 60 and grade <= 100:
    print("Pass")
else:
    print("Invalid Grade!")
