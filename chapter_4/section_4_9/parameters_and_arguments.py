# Chapter 4 - Functions
# 4.9 Parameters and arguments

# Example 1 - Pass an argument to a function
# input - A function called print_twice that takes 1 argument
# assigns the argument to a parameter named bruce
# output - When the function is called, it prints the value of the parameter that was passed in twice.
def print_twice(bruce):
    print(bruce)
    print(bruce)

# call the function called print_twice and pass it the string Spam as an argument.
print_twice('Spam')

# call the function called print_twice and pass it the string Spam multiplication as an argument.
# In the string multiplication it takes the string 'Spam' and repeats it four times,
# resulting in the new string 'SpamSpamSpamSpam'
print_twice('Spam'*4)

# example of using a variable in a function call
# create a variable called michael and assign it a string
michael = 'Eric, the half a bee.'
# call the function called print_twice and pass it the value stored in variable calle michael
print_twice(michael)
