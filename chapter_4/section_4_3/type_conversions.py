# Chapter 4 - Functions
# 4.3 Type conversion functions

# Example 1 - Convert a string into an integer
# The int function gets the argument passed in and converts it to an integer
# If the int function cant convert it, then it returns an error.
print('This is an integer converted to a string: ',int('32'))
# Displays the data type of the value returned by the int function
# In this case since the string 32 was converted to integer the type displayed should be int
print(type(int('32')))

# Example 2 - Convert a floating point number into an integer
# The int function gets the argument passed in and converts it to an integer
# When converting floating point number using int, it doesn’t round off the value, it chops off the fraction part
# If the int function cant convert it, then it returns an error.
print('float number: ',3.99999)
# Displays the data type of the value returned by the int function
# In this case since the integer 3.99999 was converted to integer the decimal .99999 gets chopped off and 3 is returned.
print('converted to an integer using the int function is: ',int(3.99999))

# Example 3 - Convert an integer to a float
print('This is integer 32 converted to a float: ',float(32))

# Example 4 - Convert a string to a float
print('This is a string converted to a float: ',float('3.14159'))

# Example 5 - Convert an integer to a string
print('This is integer 32 converted to a string: ',str(32))

# Example 6 - Convert a float to a string
print('This is float 3.14159 converted to a string: ',str(3.14159))