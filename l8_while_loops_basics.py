"""
With the while loop we can execute a set of statements as long as a condition is true.
while True - is the syntax for an endless loop!
"""

# A basic while loop will look like that:
num = 0
while num < 10:  # this loop will stop running when num == 10 or num > 10
    print(num)  # this loop will print us the numbers from 0-9
    num += 1

# An endless loop that ends when we write "bye":
while True:
    txt0 = input("If you want to exit, enter 'bye': ")
    if txt0 == "bye":
        break  # When we'll write this line in any loop, when we get to it, we'll exit the loop immediately
