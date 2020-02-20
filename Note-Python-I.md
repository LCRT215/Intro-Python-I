Data Structures

- [ Lists ]
  are what they seem - a list of values. Each one of them is numbered, starting from zero - the first one is numbered zero, the second 1, the third 2, etc. You can remove values from the list, and add new values to the end. Example: Your many cats' names. (Think JS arrays)

- ( Tuples )
  are just like lists, but you can't change their values (immutable). The values that you give it first up, are the values that you are stuck with for the rest of the program. Again, each value is numbered starting from zero, for easy reference. Example: the names of the months of the year.

- { Dictionaries }
  are similar to what their name suggests - a dictionary. In a dictionary, you have an 'index' of words, and for each of them a definition. In python, the word is called a 'key', and the definition a 'value'. The values in a dictionary aren't numbered - tare similar to what their name suggests - a dictionary. In a dictionary, you have an 'index' of words, and for each of them a definition. In python, the word is called a 'key', and the definition a 'value'. The values in a dictionary aren't numbered - they aren't in any specific order, either - the key does the same thing. You can add, remove, and modify the values in dictionaries. Example: telephone book. (Think JS objects)

Functional Arguments

- Positional Arguments
    an argument that is not a keyword argument. Positional arguments can appear at the beginning of an argument list and/or be passed as elements of an iterable preceded by *. A positional argument is any argument that's not supplied as a key=value pair.

- Arbitrary Arguments
    Sometimes, we do not know in advance the number of arguments that will be passed into a function.Python allows us to handle this kind of situation through function calls with arbitrary number of arguments.
    In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument.

- Keyword Arguments
    an argument preceded by an identifier (e.g. name=) in a function call or passed as a value in a dictionary preceded by **.

- Default Arguments
  