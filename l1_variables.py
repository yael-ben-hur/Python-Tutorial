# In this code we will present the syntax for different variables' types
# In this code we'll also show how you can use the print and read commands

# In python, integer is a whole number, positive or negative, without decimals, of unlimited length
# This is an integer:

a = 5
print(a)  # this command will print us the value of a
print(type(a))  # this command will print us what is the type of var a
print()

# In python, float is a number, positive or negative, containing one or more decimals
# This is a float:

b = 13.35
print(b)  # this command will print us the value of b
print(type(b))   # this command will print us what is the type of var b
print()  # this command will print us a blank line, it's like pressing on Enter

# In python, string is a bunch of chars surrounded by either single quotation marks, or double quotation marks.
# Strings in Python are arrays of bytes representing unicode characters.
# This is a string:

c = "morning"
print(c)  # this command will print us the value of c
print(type(c))  # this command will print us what is the type of var c
print()

# Printing strings variables with strings will look like that:
print("Good " + c)

# Printing int/float variables with strings will look like that:
print("I bought " + str(a) + " Jonathan apples for " + str(b) + " shekels!\n")
# the str(variable) command, turns a variable of any kind to a string, however it doesn't change the variable type!
# the \n in the string stands for Enter

# How to receive a string from the user
mail = input("Please enter your mail here:")
print(mail)
print(type(mail))


