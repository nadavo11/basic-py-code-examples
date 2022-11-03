"""
________________________________________________________________________________________


                                   Exercise 7

        Implement a function that takes as input three variables and returns the largest
        of the three. Do this without using the Python max() function !
        The goal of this exercise is to think about some internals that Python normally
        takes care of for us. All you need is some variables and if statements.

________________________________________________________________________________________
"""


def best_of_3(i, j, k):
    if i > j:
        return i if i > k else k
    else:
        return j if j > k else k


i = input("\ni:\t")
j = input("\nj:\t")
k = input("\nk:\t")

print(best_of_3(i, j, k))
