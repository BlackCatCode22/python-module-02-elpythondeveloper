# Chapter 4 - Functions
# 4.6 Adding new functions

# Example 1 - Defining a function
# define a function called print_lyrics
# input - The function does not take in any arguments
# output - The function does not return a value. It displays two strings in the console.
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

# Call the function called print_lyrics and display the output in the console.
# Since the function does not return a value but prints two strings, the strings are displayed.
print_lyrics()

# Example 2 - Use a function inside another function
# define a function called repeat_lyrics
# input - The function does not take in any arguments
# output - The function does not return a value. It calls the function print_lyrics twice
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# Call the function called repeat_lyrics and display the output in the console.
repeat_lyrics()