"""
Python has a built-in module that you can use to make random numbers.
It is called random.
In this lesson we will learn how to generate a random number.
"""

# Importing a function from the random module that'll let us generate random numbers to our project:
from random import randint

# Printing a random number from 1-6(including both), in each run of the program the number will be different:
print(randint(1, 6))

"""
If we want to import more than one tool of the random module, we will import random and not randint from random, and it
will give us all of the options that are available under the module.
"""
