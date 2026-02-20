# Example 1: Importing a Whole Module
import math

print(math.sqrt(16))

# Example 2: Importing Specific Functions
from datetime import datetime

print((datetime.now()))

# Example 3: Importing with an Alias
import statistics as stats

numbers = [1, 2, 3, 4, 5]
print(stats.mean(numbers))

# Example 4: Importing the custom modile and using its functions
import mymodule

mymodule.hello_name("Alice")

# Example 5: Using Built-in Modules for Practical Tasks
import os
import sys

print(os.name)
print(sys.argv)

# Example 6: Handling Import Errors
try:
    import ndasas
except ImportError as e:
    print(f"Error importing module: {e}")

# Exercise 1: calculate_circle_area(radius) that uses the math module to calculate
# and return the area of a circle given its radius.
def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2

# Exercise 2: get_current_year() that uses the datetime module to return the current year.
def get_current_year() -> int:
    return datetime.now().year
