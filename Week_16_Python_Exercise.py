# 1. Formatted Twinkle Poem
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are\n")

# 2. Circle Area Calculator
import math

# Prompt user for radius
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)  # Calculate area of the circle
print(f"r = {radius}")
print(f"Area = {area}")

# 3. Number Expansion Calculator
# Prompt user for the integer input
n = input("Enter an integer value for n: ")
# Compute n + nn + nnn
expanded_value = int(n) + int(n*2) + int(n*3)
print(f"Result: {expanded_value}")
 
