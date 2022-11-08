"""
______________________________________________________________________________

                                EX 1

        asks the user to enter their name and their age. Print out
        a message addressed to them that tells them the year that
        they will turn 100 years old .
_____________________________________________________________________________
"""

# take user's input
age = input("Hello dear user. please input your age:\n")
print(f'"you will celebrate your 100\'th anniversary in the year {2022 +100 - int(age)}')
