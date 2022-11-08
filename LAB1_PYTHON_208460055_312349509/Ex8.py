"""
________________________________________________________________________________________


                                     Exercise 8

        Given two txt files that have lists of numbers in them, find the numbers that are
        overlapping.


________________________________________________________________________________________
"""

with open('primes.txt', 'r') as f:
    primes_txt = f.read()

with open('happy.txt', 'r') as f:
    happy_txt = f.read()


primes_txt, happy_txt = primes_txt.split(), happy_txt.split()

print("overlapping numbers:")
for p in primes_txt:
    if p in happy_txt:
        print(int(p))