"""
A function is a block of code which only runs when it is called.=
You can pass data, known as parameters, into a function.
A function can return data as a result.

In Python a function is defined using the def keyword:
"""


# A function can be a function which doesn't get a value and doesn't return a value:
def dont_get_and_dont_return():
    print("This function didn't get any value, and didn't return any value!\n")


# A function can be a function which gets a value and doesn't return a value:
def get_and_dont_return(val):
    print("This function did get a value, and didn't return any value!\n")
    print("This is the value: " + str(val) + "\n")


"""
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just
separate them with a comma.
Arguments are often shortened to args in Python documentations.

From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 
arguments, you have to call the function with 2 arguments, not more, and not less.

If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the 
function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly

You can also send arguments with the key = value syntax.
When key is the parameter and value is the argument.
This way the order of the arguments does not matter.

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the 
parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly
Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
In python, you don't have to declare a kwargs when you call a function but if you need it you will call using the key
value syntax.

"""

# A function that get multiple argument using * :


def kids(*kids_name, food, **high):
    print("The kids' names are: " + str(kids_name))
    print("They love to eat: " + food)
    print(high)


# A function can be a function which gets a value and returns a value:
def get_and_return(val):
    print("This function did get a value, and it return a value as well!\n")
    return [str(val), "hi"]


# A function can be a function which gets a value and returns a value:
def dont_get_and_return():
    print("This function did not get a value, but it returns a value!\n")
    return "Yael is the queen"


# Calling different types of functions:
dont_get_and_dont_return()
get_and_dont_return("Yael")
print("This is the value that we got: " + str(get_and_return("HI")) + "\n")
print("This is the value that we got: " + str(dont_get_and_return()) + "\n")
kids("Yael", "Yoni", "Waffle", food="waffles", high="This is a kwarg")
