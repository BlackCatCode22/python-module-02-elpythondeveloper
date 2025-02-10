# Chapter 4 - Functions
# 4.5 Random number

# Import the random module
# This module provides functions for generating pseudo-random numbers,
# as well as other random-related operations (like shuffling sequences).
import random

# Example 1 - Generate a list of 10 random numbers between 0.0 and up to but not including 1.0.
for i in range(10):
    x = random.random()
    print(x)