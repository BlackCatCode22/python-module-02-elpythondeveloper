# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 2 - Chapter 4 Functions
# Exercise 04_06: Rewrite your pay computation with time-and-a-half for over-time
# and create a function called computepay which takes two parameters (hours and rate).
#
# Example Input and Output:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# ----- Function - computepay -----
# input - Takes 2 float arguments called hours and rate
# output - The function returns the total pay.
def computepay(hours, rate):
    # print("In computepay", hours, rate)
    # check if employee worked more than 40 hours
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print("Returning",pay)
    return pay
# ----- Function - computepay -----

# ----- Section 1 - Get Input -----
# Display a string to the user. Then have the user input the answer on the same line.
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# ----- Section 1 - Get Input -----

# ----- Section 2 - Display Output -----
# Call the function called computepay and pass it the values stored in variables fh and fr.
# The value returned by the function is then stored in variable xp.
xp = computepay(fh, fr)
# Display the value stored in variable xp in the console.
print("Pay:", xp)
# ----- Section 2 - Display Output -----
