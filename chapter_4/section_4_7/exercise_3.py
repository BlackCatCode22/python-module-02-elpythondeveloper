# Chapter 4 - Functions
# 4.7 Definitions and uses

# Exercise 3 - Move the function call back to the bottom and move the
# definition of print_lyrics after the definition of repeat_lyrics. What
# happens when you run this program?
# Output:
# Get the same output after changing the order of repeat_lyrics and print_lyrics.
# Their order does not matter.

# define a function called repeat_lyrics
# input - The function does not take in any arguments
# output - The function does not return a value. It calls the function print_lyrics twice
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# define a function called print_lyrics
# input - The function does not take in any arguments
# output - The function does not return a value. It displays two strings in the console.
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

# Call the function called repeat_lyrics and display the output in the console.
repeat_lyrics()