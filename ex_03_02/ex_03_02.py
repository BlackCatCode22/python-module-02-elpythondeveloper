# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Exercise 03_02: Rewrite your pay program using try and except so that your
#                 program handles non-numeric input gracefully by printing a message
#                 and exiting the program.
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
try:
    # convert input string values to float values
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

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
