"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

In this lesson we will focus on conditions in if statements.

Condition get the value "True" when the current situation applies to it, when it does not it gets the value - "False"

Python uses indention for keeping the code organized and nice looking to the eye, instead of using brackets like many
other coding languages. It is recommended to use a tab/4 spaces when writing if statements, functions, loops or classes
in Python:)
"""

# Equals condition in an if statement:
name = input("Please enter your first name: ")
if name == "Yael":
    print("Hi Yael!")  # If the result of the condition is True, we will get here.
else:
    print("Hi " + name + "!")  # If the result of the condition is False, we will get here.

# Greater than / Equals to condition in an if statement:

age = int(input("Please enter your age (in numbers): "))
if age >= 21:
    # If the value of age is equal or bigger than 21, we'll get here.
    print("You are allowed to drink alcohol in the United States!\n")
else:
    # If the result of the condition is False, we will get here.
    print("You are not allowed to drink alcohol in the United States!\n")

# If statements inside each other:
# (We can see the use of indention in the following example)
name = input("Please enter your first name: ")
if name == "Yael":
    print("Hi Yael!")  # If the result of the condition is True, we will get here.
    age = int(input("Please enter your age (in numbers): "))
    if age <= 18:
        # If the value of age is equal or bigger than 21, we'll get here.
        print("You are underage!\n")
    else:
        # If the result of the condition is False, we will get here.
        print("You are not underage!\n")
else:
    print("Where is Yael?\n")  # If the result of the condition is False, we will get here.

# Greater than to condition in an if statement:
num = int(input("Please enter a number: "))
if num > 3:
    print(str(num) + " * 2 = " + str(num*2))
else:
    print(str(num) + " * 3 = " + str(num*3))
print()

"""
Logical conditions:

and 	Returns True if both statements are true		
or	Returns True if one of the statements is true		
not	Reverse the result, returns False if the result is true	
"""

# and logical condition in an if statement:
name = input("Please enter your first name: ")
age = int(input("Please enter your age (in numbers): "))

if (name == "Yael") and (age >= 18):
    print("You can enter the club!\n")
else:
    print("You are not allowed to enter the club!\n")

# or logical condition in an if statement:
name = input("Please enter your first name: ")
age = int(input("Please enter your age (in numbers): "))

if (name == "Yael") or (age >= 18):
    print("You can enter the club!\n")
else:
    print("You are not allowed to enter the club!\n")

# not logical condition in an if statement:
name = input("Please enter your first name: ")
if not name == "Yael":
    print("You are a bad dancer!")
else:
    print("You are a great dancer!")




