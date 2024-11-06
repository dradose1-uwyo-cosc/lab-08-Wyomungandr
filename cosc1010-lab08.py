# Andrew Sharum
# UWYO COSC 1010
# 05NOV24
# Lab 08
# Lab Section:11
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def convert_string(s):
    try:
        # Try to convert to an integer
        return int(s)
    except ValueError:
        pass
    
    try:
        # Check if the string is a float with one decimal point
        if s.count('.') == 1:
            return float(s)
    except ValueError:
        pass
    
    # Return False if the string cannot be converted to an int or float
    return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def slope_intercept(m, b, lower_bound, upper_bound):
    # Check if bounds are integers
    if not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
        return False
    
    # Check if lower bound is less than or equal to upper bound
    if lower_bound > upper_bound:
        return False
    
    # Calculate y values for the given x range
    y_values = []
    for x in range(lower_bound, upper_bound + 1):
        y = m * x + b
        y_values.append(y)
    
    return y_values

while True:
    # Prompt user for input
    m_input = input("Enter the slope (m): ")
    b_input = input("Enter the intercept (b): ")
    lower_bound_input = input("Enter the lower x bound: ")
    upper_bound_input = input("Enter the upper x bound: ")
    
    # Exit the loop if user types "exit"
    if m_input.lower() == "exit" or b_input.lower() == "exit" or lower_bound_input.lower() == "exit" or upper_bound_input.lower() == "exit":
        break
    
    # Convert inputs to appropriate types
    try:
        m = float(m_input)
        b = float(b_input)
        lower_bound = int(lower_bound_input)
        upper_bound = int(upper_bound_input)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    
    # Call the slope_intercept function and print the result
    result = slope_intercept(m, b, lower_bound, upper_bound)
    print(result)
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
while True:
    # Prompt user for input
    a_input = input("Enter the coefficient a: ")
    b_input = input("Enter the coefficient b: ")
    c_input = input("Enter the coefficient c: ")
    
    # Exit the loop if user types "exit"
    if a_input.lower() == "exit" or b_input.lower() == "exit" or c_input.lower() == "exit":
        break
    
    # Convert inputs to appropriate types
    try:
        a = float(a_input)
        b = float(b_input)
        c = float(c_input)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    
    # Call the quadratic_formula function and print the result
    result = quadratic_formula(a, b, c)
    if result is None:
        print("No real solutions.")
    else:
        print(f"The solutions are: {result[0]} and {result[1]}")