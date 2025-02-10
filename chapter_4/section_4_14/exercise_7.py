# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 2 - Chapter 4 Functions
# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
#
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
#
#Example Input and Output
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F

# ----- Function - computegrade -----
# Function to compute the grade based on the score
# input - Takes 1 float argument called score
# output - The function returns a string holding the letter grade for the input score
def computegrade(score):
    if score < 0.0 or score > 1.0:
        return 'Bad score'  # Return "Bad score" directly
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:  # Simplified conditions
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:  # No need for another condition
        return 'F'
# ----- Function - computegrade -----

# Display a string to the user. Then have the user input the answer on the same line.
# The input is saved as a string in variable called string_input_score
string_input_score = input('Enter score: ')
# print('You entered a score of:', string_input_score)
try:
    # convert input string value to float value
    float_input_score = float(string_input_score)

    if float_input_score < 0.0 or float_input_score > 1.0:
        raise ValueError('Score must be between 0.0 and 1.0')

    # Call the function called computegrade and pass in the value stored in variable float_input_score
    # The value returned by the function is stored in the variable called grade
    grade = computegrade(float_input_score)
    # Print the value stored in the variable called grade
    print(grade)

except ValueError:
    # If there is an error in the try block then this string will be displayed in the console
    print('Bad score')
