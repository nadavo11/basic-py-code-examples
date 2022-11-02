"""
______________________________________________________________________________

                                EX 5

Ask the user for a number and determine whether the number is prime or not.
(A prime number is a number that has no divisors.).
You may use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions.

_____________________________________________________________________________
"""




import math


def is_prime(n):
    # look for divisors:
    for i in range(2, int(math.sqrt(n))):
        # if we find one, then n isn't prime, is it?
        if not n % i: return False

    return True


# get user input, cast to int!
n = int(input("Hello dear user. please choose a positive whole number of your choice:\n"))

# print the result
if is_prime(n):
    print("prime")
else:
    print("not prime")
