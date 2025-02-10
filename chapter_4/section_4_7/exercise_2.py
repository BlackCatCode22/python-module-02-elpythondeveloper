# Chapter 4 - Functions
# 4.7 Definitions and uses

# Exercise 2 - Move the last line of this program to the top, so the function
# call appears before the definitions. Run the program and see what error
# message you get.
# Output:
# After running the programming gets this error:
# NameError: name 'repeat_lyrics' is not defined

# Moved the last line of this program to the top
# Call the function called repeat_lyrics and display the output in the console.
repeat_lyrics()

# define a function called print_lyrics
# input - The function does not take in any arguments
# output - The function does not return a value. It displays two strings in the console.
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

# define a function called repeat_lyrics
# input - The function does not take in any arguments
# output - The function does not return a value. It calls the function print_lyrics twice
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

