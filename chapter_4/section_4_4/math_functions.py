# Chapter 4 - Functions
# 4.4 Math Functions

# before we can use math function we need to import the math module
import math

# Example 1 - display information about the math module
# The module object contains the functions and variables defined in the module.
# To access one of the functions, you have to specify the name of the module and the
# name of the function, separated by a dot (also known as a period).
print(math)

# Example 2 - Computes the logarithm base 10 of the signal-to-noise ratio.
# store the value 1 milliwatt in variable signal_power
signal_power = 0.001
# #store the value  0.01 milliwatt in variable noise_power
noise_power = 0.00001
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print('The logarithm base 10 of the signal-to-noise ratio is: ', decibels)

# Example 3 - Find the sine of radians
radians = 0.7
height = math.sin(radians)
print('The sine of radians is: ', height)