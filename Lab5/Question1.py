def finalGrade(exam, hw):
    if exam >= 50 and hw > exam:
        fGrade = exam * 0.75 + hw * 0.25
    else:
        fGrade = exam
    return int(fGrade)


grade1 = finalGrade(50, 90)
grade2 = finalGrade(90, 100)

print(grade1)
print(grade2)
