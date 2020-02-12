# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]

# The append() method adds an item to the end of the list.

x.append(4)
print("- Append:", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]

# The extend() extends the list by adding all items of a list (passed as an argument) to the end. The extend() method only modifies the original list. It doesn't return any value.

x.extend(y)
print("- Extend:", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# The remove() method removes the first matching element (which is passed as an argument) from the list.

x.remove(8)
print("- Remove:", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# The insert() method inserts an element to the list AT a given index.

x.insert(5, 99)
print("- Insert:", x)

# Print the length of list x
# The len() function returns the number of items (length) in an object.

print("- The length of x is:", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

for i in x:
    multi = i * 100
    
print("- Using a for loop", multi)
# print(list(range(1,22)))
