string = input("Roman Numeral:")
def roman(string):
    total = 0
    romandict = {
        "I" : 1,
        "IV" : -1,
        "V" : 5,
        "IX" : -1,
        "X" : 10,
        }
    for x in string:
       total += romandict[x]

    return print(total)

