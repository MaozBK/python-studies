def BMIcalculator(weight, height):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        bmiState = "Underweight"
    elif bmi > 18.5 and bmi < 24.9:
        bmiState = "Normal Weight"
    elif bmi > 25.0 and bmi < 29.9:
        bmiState = "Increased Weight"
    elif bmi > 30 and bmi < 39.9:
        bmiState = "Obese"
    else:
        bmiState = "Very high Obese"
    return bmi, bmiState


print(BMIcalculator(83, 183))
print(BMIcalculator(140, 180))
