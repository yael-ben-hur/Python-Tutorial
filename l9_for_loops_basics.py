"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in
other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

# For loop when the iterator is a number in range of numbers:
for x in range(10):
    print(x)  # this loop will print us the numbers from 0-9
print()

# For loop when the iterator is an element in a list:
list0 = ["Lital", "&", "Yael", "are the best cousins"]
for x in list0:
    print(x)  # this loop will print us the list elements, one by one
print()

# For loop when the iterator is a place in a list:
for x in range(len(list0)):
    print(x)  # this loop will print us number from 0-[len(list0)-1]
print()

# For loop when the iterator's value rises in 2 every time
for x in range(0,10,2):  # as we can see, the syntax to add 2 everytime is by adding the value 2 to the third int
    print(x)  # this loop will print us the even numbers from 0-8
