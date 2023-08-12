# In this code we will learn how to do basic Math in Python

# First of all, we'll define an integer and print it
num1 = 5
print("Your number is: " + str(num1) + ".")

# Next, we'll see how you can do addition to an integer:
num1 = num1 + 2  # first syntax of doing addition to our integer
print("Your number is: " + str(num1) + ".")
num1 += 2  # second syntax of doing addition to our integer
print("Your number is: " + str(num1) + ".")

# You can also use one integer to define another integer
# Here we will show you how you can do subtraction from one int, and entering the value to another int:
num2 = num1 - 2
print("Your 2nd number is: " + str(num2) + ".")

num2 -= 2  # another subtraction syntax
print("Your 2nd number is: " + str(num2) + ".")

# In order to do multiplication on an integer we can write the following syntax:
num2 = num2 * num1
print("Your 2nd number is: " + str(num2) + ".")

num2 *= 2  # another multiplication syntax
print("Your 2nd number is: " + str(num2) + ".")

# Division looks like that:
num2 = num2/num1
print("\n90/9 equals: " + str(num2))
# Even if we divide 2 integers, the result of division will always be float
print("The type of the result is: " + str(type(num2)) + ".\n")

num2 /= 2  # another syntax for division
print("The result of 10/2 is: " + str(num2) + " .\n")

# Division without a reminder
num3 = num1 // num2
num4 = num1 / num2
print("The division of 9/5 without a reminder is: " + str(num3) + " .")
print("The division of 9/5 with a reminder is: " + str(num4) + " .\n")

num1 = 8
num2 = 3
num1 //= num2  # another syntax for division without a reminder
print("The division of 8/3 without a reminder is: " + str(num1) + " .\n")

# Using modulo to find the reminder of a division:
num1 = 9
num2 = 5
num3 = num1 % num2
print("The reminder of 9/5 is: " + str(num3) + " .")
num1 = 8
num2 = 3
num3 = num2 % num1
print("The reminder of 3/8 is: " + str(num3) + " .\n")

# Now will we show you how you can do exponentiation:
base = 3
exponent = 2

result = base ** exponent
print("The result of " + str(base) + "^" + str(exponent) + " is: " + str(result))

result = 4
result **= exponent # another syntax
print("The result of 4^" + str(exponent) + " is: " + str(result))





