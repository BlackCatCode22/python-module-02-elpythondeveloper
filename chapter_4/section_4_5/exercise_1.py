# Chapter 4 - Functions
# 4.5 Random number

# Exercise 1

# Import the random module
# This module provides functions for generating pseudo-random numbers,
# as well as other random-related operations (like shuffling sequences).
import random

# Exercise 1: Run the program on your system and see what numbers you get.
# Run the program more than once and see what numbers you get.
# Takes two integer arguments, a and b,
# and returns a random integer N such that a <= N <= b.
# Both a and b are included in the possible range of values.
# 1st run
print(random.randint(5,10))
# 2nd run
print(random.randint(5,10))


#To choose an element from a sequence at random, you can use choice:
t = [1, 2, 3]
# 1st run
print(random.choice(t))
# 2nd run
print(random.choice(t))