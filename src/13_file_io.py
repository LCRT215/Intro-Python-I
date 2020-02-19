"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

foo = open(
    "/Users/lesliethompson/CODE/Lambda School/CS Projects/Intro-Python-I/src/foo.txt", "r")

print(foo.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open(
    "/Users/lesliethompson/CODE/Lambda School/CS Projects/Intro-Python-I/src/bar.txt", "w")

bar.write('Leslie is the besttttt.') 
bar.write('\n She is pretty awesome.')
bar.write('\n So hire her asap 😐.') 

bar.close()




# YOUR CODE HERE
