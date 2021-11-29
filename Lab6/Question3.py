table = [[6, 9, -18, 12, 21],
         [5, 20, 0, 4, 16],
         [-6, 5, -12, -6, -13]]


def tableSum(table):
    sum = 0
    for list in table:
        for i in list:
            sum += i
    return sum


def maxInTable(table):
    max_Num = 0
    for list in table:
        for i in list:
            if i > max_Num:
                max_Num = i
    return max_Num

def minInTable(table):
    min_Num = 0
    for list in table:
        for i in list:
            if i < min_Num:
                min_Num = i
    return min_Num


def sortTable(table):
    row = 1
    for list in table:
        print("Row Number", row, " after sorting: ", sorted(list))
        row += 1


print("The Sum is: ", tableSum(table))
print("The Max number is:", maxInTable(table))
print("The Min numberis: ", minInTable(table))
print(sortTable(table))
