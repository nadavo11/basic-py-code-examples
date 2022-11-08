"""
______________________________________________________________________________

                                EX 5


Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols.
The passwords should be random, generating a new password every time the
user asks for a new password.
Include your run-time code in a main method1

_____________________________________________________________________________
"""
import random

#familliar with ASCII code yet?
valid_chars = range(33,126)

password = ""
for i in range(16):
    password = password+(chr(random.choice(valid_chars)))

print(f'your new password is: {password}')