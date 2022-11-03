"""
________________________________________________________________________________________


                                     Exercise 10

        Given an unsorted array of positive and negative numbers and another number
        X. Write a function that checks if there is a pair of numbers in the array whose
        sum is equal to the number X. It is enough to return True/False answer.

________________________________________________________________________________________
"""


def is_x_in_l(L, x):
    for l in L:
        if (x - l) in L:
            return True
    return False


print(is_x_in_l([1, 3, -4], -3))
