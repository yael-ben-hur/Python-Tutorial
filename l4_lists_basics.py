"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and
Dictionary, all with different qualities and usage.

Lists are created using square brackets
"""

# Creating an empty list can be done in two ways:

# First way:
list0 = []
print("The variable list0 is: " + str(type(list0)))  # we will see that the type of list0 is list
print()

# Second way:
list1 = list()
print("The variable list1 is: " + str(type(list1)))  # we will see that the type of list1 is list
print()

# Creating a list with variables:
list0 = [2, 3, 6, "Yael Ben Hur", []]

# Printing the list values:
print(list0)

# Adding variables to a list can be done in two ways:

# 1st way:
list0 = list0 + [99]
print("We added to the list the integer 99: " + str(list0))

# 2nd way:
list0 += ["hi"]
print("We added to the list the string 'hi': " + str(list0) + "\n")

# We can also combine two lists to one list:

list1 = ["Salsa is fun", "Sam dances the worst", "I love Ariela and Neta<3"]
print("This is list0: {}\nThis is list1: {}".format(list0, list1))
list2 = list0 + list1
print("This is the combination of list0 and list1: " + str(list2) + "\n")

# We can also multiply the appearance of all the list's elements like that:

# 1st way:
list1 = list1 * 2
print(str(list1) + "\n")

list1 = ["Ofir", "Yuval", "Shachar"]
print("This is list1: {}".format(list1))
# 2nd way:
list1 *= 3
print("This is list1*3: {}".format(list1))

'''
If we want to print a specific element in our list, we'll print it the same way we want to print an element from a 
string - list[n].
In list the counting of element from the beginning also begins with 0 and end with len(list)-1
We can also count the list elements in a reversed order [from -1 to -len(list)].
And that's it!
'''

# Example of printing that last element of list1:
print("My youngest nephew is: " + list1[-1] + ".")

'''
If we want to print an str element in a list with another string, we don't have to define it as a string because it is
already a string.
'''
# example of printing a str element with another string:
print("My niece is " + list1[1] + ".\n")

# Breaking a string to a list of chars will be done like that:
str0 = "abcdefg"
list0 = list(str0)  # this action will put each of the chars of the string as a separate element on the list
print("My string is: " + str0)
print("The chars of the string are: " + str(list0))

# Creating a string from a list of elements:
print("My list is: " + str(list1))
str1 = ' & '.join(list1)
print("I am using the string ' & ' to separate my list's elements in the string I'll create from it!")
print("The string I create from my list is: " + str1 + "\n")

'''
When we use the join command on a list, all of its elements got to be a string.
The join command syntax is like that: '[value]'.join([list_of_strings])
When [value] is a string that will appear between each of the list's elements (we can write nothing and then all of the
list's strings will be formed into one gibberish string), and [list_of_strings] is the list which all of its elements
are strings.
'''
# Splitting a string into a list:
print("My string is: " + str1)
list0 = str1.split()  # by default, the elements of the list will be chosen based on spaces
# meaning - each char\s in the string that are next to each other and aren't separated by spaces - will be an element
print("The list I've create from it is: " + str(list0) + "\n")

'''
If we want to choose an operator in our string that will be responsible of "cutting it" into smaller elements (meaning
it won't show up on the list in the end and the chars in the string that are separated by it will be the list elements),
we can enter the operator in the brackets the appear after the split - (), we will enter the operator as a string.
'''

# Creating a list from a string, based on a char:
print("My string is: " + str1)
list2 = str1.split(" & ")
print("The list I've create from it is: " + str(list0) + "\nI used the string ' & ' as an elements' seperator!\n")

'''
We can also create a list from a string's lines. Meaning, there is a command that will make our list's elements to be
the string's lines.
'''

str0 = "Hi my name is Yael.\nI am 21 years old."
print("This is my string:\n" + str0)
list0 = str0.splitlines()
print("This is the list I created from it after using the splitlines command: " + str(list0))


# Finding the length of a list will be done like that:
print("The length of my list is: " + str(len(list0)))
# the len function returns us the number of elements that are in the list

# Adding a value to the end of a list:
list0.append("I am tired!")
print("I added a value to my list: " + str(list0))

# Adding a value to the list in a specific place:
list0.insert(1, "I am from Israel.")
print("I added to my list an element in list0[1]: " + str(list0) + "\n")

'''
Meaning, the syntax is: you enter in the brackets the place you would like to add your element then you add a comma
and then you write the element that you would like to add.
If you'll write a place which is equal to / larger than the length of the list it will be added in the last place of the
list elements. 
'''

# Removing the last element that appears in a list and getting its value will be done like that:
print("I popped the element: " + list0.pop())
print("My list's elements are now: " + str(list0))

# I can also remove a specific element and get its value from a list like that:
print("I popped the 0 element in my list: " + list0.pop(0))
print("My list's elements are now: " + str(list0) + "\n")

# Check if a variable appears in my list:
print("Does the integer 2 appears in my list?")
if 2 in list0:
    print("It does!")
else:
    print("It doesn't!")

print("Does the string 'I am 21 years old.' appears in my list?")
if 'I am 21 years old.' in list0:
    print("It does!")
else:
    print("It doesn't!")
