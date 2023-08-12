'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
In a dictionary we can't have more two or more values with the same name.
'''

# Defining an empty dictionary:
dict0 = {}
print("The type of dict0 is: " + str(type(dict0)))

# Another way for defining an empty dictionary:
dict0 = dict()
# When we'll run the program we'll see that we have another dict here:
print("The type of dict0 is: " + str(type(dict0)) + "\n")

# Creating a dictionary with values in it:
dict0 = {"www.google.com": "8.8.8.8", "www.youtube.com": ["5.5.5.5", "4.4.4.4"]}
print("This is my dictionary: " + str(dict0))

# Adding a value to a dictionary:

# 1st way:
dict0.update({"www.net4uc.com": "33.33.33.33"})
print("I added a value to my dictionary: " + str(dict0))

# 2nd way:
dict1 = {"www.groo.co.il": "88.88.88.88"}
dict0.update(dict1)
print("I added a value to my dictionary: " + str(dict0))


# Updating a keys' values on a dictionary can be done like that:
dict1 = {"www.net4uc.com": "44.44.44.44"}
dict0.update(dict1)
print("I updated net4uc IP address: " + str(dict0) + "\n")

# Finding the length of my dictionary (the number of keys in the dictionary):
print("I have " + str(len(dict0)) + " keys in my dictionary!\n")

# Finding keys' values will be done like that:
print("The value of 'www.google.com' is: " + dict0["www.google.com"])

# Getting all of my dictionary's values will be done like that:
print("The values in my dictionary are : " + str(dict0.values()) + "\n")

# Changing a key's value/s will be done like that:
dict0["www.google.com"] = "8.8.4.4"
print("I changed Google's DNS server's IP address: " + str(dict0) + "\n")

# Finding if a key exists in my dictionary will be done like that:
if "www.google.com" in dict0:
    print("'www.google.com' is a key in my dictionary!")
else:
    print("'www.google.com' is not a key in my dictionary!")

if "www.google2.com" in dict0:
    print("'www.google2.com' is a key in my dictionary!")
else:
    print("'www.google2.com' is not a key in my dictionary!")

print()

# Finding if a value exists in my dictionary will be done like that:
if "www.google.com" in dict0.values():
    print("'www.google.com' is a value in my dictionary!")
else:
    print("'www.google.com' is not a value in my dictionary!")

if "8.8.4.4" in dict0.values():
    print("'8.8.4.4' is a value in my dictionary!")
else:
    print("'8.8.4.4' is not a value in my dictionary!")

# Printing the dictionary's keys will be done like that:
print("My dictonary keys are: " + str(dict0.keys()))
