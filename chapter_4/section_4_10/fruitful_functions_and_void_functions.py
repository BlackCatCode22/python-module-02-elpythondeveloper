# Chapter 4 - Functions
# 4.10 Fruitful functions and void functions

# Example 1 - A function called add that takes 2 arguments and adds them
# input - A function called addtwo that takes 2 arguments.
# output - The function returns the sum of the to input arguments.
def addtwo(a, b):
    added = a + b
    return added

# call the function called addtwo and pass it the arguments 3 and 5
# the value returned by the function is then stored in variable x
x = addtwo(3, 5)
# display the value stored in variable x in the console.
print(x)