# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Exercise 03_01: Rewrite your pay computation to give the employee 1.5 times
#                 the hourly rate for hours worked above 40 hours.
#
# Example Input and Output:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# ----- Section 1 - Get Input -----
# Display a string to the user. Then have the user input the answer on the same line.
sh = input("Enter Hours: ")
# Display a string to the user. Then have the user input the answer on the same line.
sr = input("Enter Rate: ")
# ----- Section 1 - Get Input -----

# ----- Section 2 - Perform Calculation -----
# convert input string values to float values
fh = float(sh)
fr = float(sr)
# print(fh, fr)

# check if employee worked more than 40 hours
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    # print("Regular pay: ",reg)
    otp = (fh - 40.0) * (fr * 0.5)
    # print("Overtime pay: ",otp)
    # print(reg,otp)
    xp = reg + otp
else:
    # print("regular")
    xp = fh * fr

# ----- Section 2 - Perform Calculation -----

# ----- Section 3 - Display Output -----
# Display the string Pay: followed by the value stored in variable total_pay in the console
print("Pay:", xp)
# ----- Section 3 - Display Output -----
