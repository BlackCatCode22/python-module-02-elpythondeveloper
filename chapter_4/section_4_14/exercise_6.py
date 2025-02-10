# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 2 - Chapter 4 Functions
# Exercise 6: Rewrite your pay computation with time-and-a-half for over-time
# and create a function called computepay which takes two parameters (hours and rate).
#
# Example Input and Output:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# ----- Section 1 - Get Input -----
# Display a string to the user. Then have the user input the answer on the same line.
prompt_hours = 'Enter Hours: '
# The input is saved as a string in variable called string_input_hours
string_input_hours = input(prompt_hours)
# convert input string values to float values
float_input_hours = float(string_input_hours)
# Display a string to the user. Then have the user input the answer on the same line.
prompt_rate = 'Enter Rate: '
# The input is saved as a string in variable called string_input_rate
string_input_rate = input(prompt_rate)
# convert input string values to float values
float_input_rate = float(string_input_rate)
# ----- Section 1 - Get Input -----

# ----- Function - computepay -----
# input - Takes 2 float arguments called hours and rate
# output - The function returns the total pay.
def computepay(hours, rate):
    # check if employee worked more than 40 hours
    if float_input_hours > 40:
        regular_hours = 40
        # Get the number of hours above 40
        overtime_hours = float_input_hours - 40
    else:
        overtime_hours = 0
        regular_hours = float_input_hours

    float_regular_pay = regular_hours * float_input_rate
    overtime_rate = float_input_rate * 1.5
    overtime_pay = overtime_hours * overtime_rate
    total_pay = float_regular_pay + overtime_pay

    return total_pay
# ----- Function - computepay -----

# ----- Section 2 - Display Output -----
# Call the function called computepay and pass it the values stored in
# variables float_input_hours and float_input_rate.
# The value returned by the function is then stored in variable x.
x = computepay(float_input_hours, float_input_rate)
# dDisplay the value stored in variable x in the console.
print("Pay:", x)
# # Display the string Pay: followed by the value stored in variable total_pay in the console
# print("Pay:", total_pay)
# ----- Section 2 - Display Output -----