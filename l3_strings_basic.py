# In this lesson we will learn basic string rules

# The most basic syntax of a string
str0 = "abc"

# If we want to add an Enter in the middle of a string, we can add the sign "\n" - \n = Enter
str1 = "I want to begin a new line,\nI did it!\n"
print(str1)

# There's another way to press Enter in the middle of the string, and it is done by defining it with ''' :
str2 = '''I want to begin a new line,
I did it!
'''
print(str2)

# You can see that str1 and str2 are the same string by writing the next command:
print("Both of the strings are the same: " + str(str2 == str1))

# If we want to enter values into a string we can do it in two ways!

# The first one, is defining variables and additing them to the string.

name = "Yael"
age = 21
str3 = "\nMy name is: " + name + ".\nI am " + str(age) + " years old."
print(str3)

# The second way, is by using the format command:
str3 = "\nMy name is: {}.\nI am {} years old."
print(str3.format(name, age))

'''
The format commands means, that for each curly brackets we enter a value.
Meaning if we have 3 curly brackets, we will enter 3 variables to our choice and the format command
will turn them to a string in case they are not a string.
'''

# If we want to check if a substring appears in a string, we can use the "in" command like so:
# The result that will be printed is True, because the substring Ben appears in Yael Ben Hur:
print("Ben" in "Yael Ben Hur")

# The result that will be printed here is False, because the substring Eladi doesn't appear in Yael Ben Hur:
print("Eladi" in "Yael Ben Hur")

# We can also use string variables with the in command
full_name = "Yael Ben Hur"
print(name in full_name)  # The result will be true

'''
Choosing a char from the string would be in this syntax: str[n] when n can be any integer, positive or negative
and its absolute value can't be bigger or equal to the string's length. 
'''

# We can print the string's first char like that:
print(full_name[0])
# Or like that:
print(full_name[-len(full_name)])
print()

# We can print the string's last char like that:
print(full_name[-1])
# Or like that:
print(full_name[len(full_name)-1])
print()
'''
We can see from the example that we showed, that we can count the string's chars from 0 (which is the first char) 
to [len(str)-1] (which is the last char) or from -1 (which is the last char) to [-len(str)] (which is the first char).
'''

# We can also choose a part of the string, part of the string is called substring.
# If we want to print from the string full_name only the last name, we will write this command:
print(full_name[5:len(full_name)])
# Or like that:
print(full_name[5:])

# If we write it like this:
print(full_name[5:-1])
'''
The last letter of the string won't be printed. Meaning, if we had an upper limit, the letters from the lower limit
including the lower limit - will be printed until 1 char before the upper limit.
In simple words - if we had upper limits, the char under its number and the chars after it - won't show up. 
If we won't add a lower limit, the substring will begin in the beginning of the string.
If we won't add an upper limit, the substring will end with the last char of the string (included).
'''

# If we want to see the chars that appears only in the even places in the string we will write:
print(full_name[::2])

'''
Meaning, if we want our substring to be formed out of certain hops over the string we can add a third colon and after
him the size of the hop that we want.
We can also give the hop a negative value and that will make the substring "choose" the letters from the string from its
ending to its beginning
'''

# For example if we want to see how my name is spelled backwards, we will write the next command:
print(full_name[::-1])