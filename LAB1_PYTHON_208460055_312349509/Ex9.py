"""
________________________________________________________________________________________


                                     Exercise 9

    Write a function that gets a sorted list of numbers and another number X. The
    function decides whether or not the given number X is inside the list or not and
    returns True/False answer.

________________________________________________________________________________________
"""


def is_in_l(l, x):
    """input:
                -l:  list
                -x:  a value tolook for in l"""
    return x in l


print(is_in_l([1, '', 3, '2'], 2))
