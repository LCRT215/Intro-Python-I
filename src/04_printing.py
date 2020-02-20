"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("This is from the printf operator method", "x is %s, y is %s, z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing

string2 = "x is {}, y is {}, z is {}".format(x, y, z)
print("This is the 'format' string method:", string2)

# Finally, print the same thing using an f-string WAS ADDED IN PYTHON VERSION 3.61

fString = f"x is {x}, y is {y}, z is {z}"
print("This is the fString method:", fString)