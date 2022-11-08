"""
________________________________________________________________________________________


                                     Exercise 8

        You should generate the txt files by yourself (using python, not manually): One
        txt file has a list of all prime numbers under 1000, and the other txt file has a list
        of happy numbers up to 1000 .
        [Prime numbers are numbers that can’t be divided by any other number. Yes,
        Happy numbers are a real thing in mathematics - you can look it up on
        Wikipedia]

________________________________________________________________________________________
"""

from Ex4 import is_prime


def get_all_primes_until(n):

    # starting condition: maintain a list of all primes so far
    return [i for i in range(2, n + 1) if is_prime(i)]

def pdi_function(number, base: int = 10):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total += pow(number % base, 2)
        number = number // base
    return total

def is_happy(number: int) -> bool:
    """Determine if the specified number is a happy number."""
    seen_numbers = set()
    while number > 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = pdi_function(number)
    return number == 1

def get_all_happy_until(n):

    # starting condition: maintain a list of all primes so far
    return [i for i in range(2, n + 1) if is_happy(i)]


primes = get_all_primes_until(1000)
happy = get_all_happy_until(1000)

# open a new primes txt file
with open('primes.txt','w') as f:
    # insert all primes, separated by blanks
    for p in primes:
        f.write(f'{p} ')

# same for happy nums
with open('happy.txt','w') as f:
    for h in happy:

        f.write(f'{h} ')
