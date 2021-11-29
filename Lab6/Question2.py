
beatles = ["John Lennon", 1940, "England", "Paul McCartney", 1942, "England", "George Harrison", 1943, "England",
           "Ringo Starr", 1940, "England"]


def printMembers(list):
    count = 1
    band = "Member " + str(count) + ": ['"
    for i in beatles:
        if 'England' in str(i):
            band = band + " " + str(i) + "']"
            print(band)
            count = count + 1
            band = "Member " + str(count) + ": ['"
        else:
            band += " " + str(i)

# your code here

printMembers(beatles)
