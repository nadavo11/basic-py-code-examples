"""
______________________________________________________________________________

                                EX 2

        asks the user for a number and then prints out a list of
        all the divisors of that number.

_____________________________________________________________________________
"""
import math
n = 0

while n <= 0:
    n = int(input("Hello dear user. please choose a positive whole number of your choice:\n"))
    if n <= 0 :
        print("WHY YOU NO PUT VALID INPUT")


divisors = [i for i in range(2, int(math.sqrt(n))) if not n % i]


print(f'here are all of {n}\'s divisors:  {divisors}')
