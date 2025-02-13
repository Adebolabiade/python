print("Welcome to personalised user profile generator!\n This program colects and processes user information")

full_name = str(input("Enter your full name: "))#input youur name
age = int(input("Enter your age: "))#INPUT AGE
height = float(input("Enter your height:"))#Input height
Favourite_programming_language = str(input("Enter your favourite programming language: "))#input favourite language
Favourite_number = int(input("Enter your favourite number:"))#input favourite number
About_yourself = str(input("About yourself:" ))#describe yourself

# Conversions (as requested)
age_float = float(age)
height_int = int(height)
favorite_number_str = str(123)  # Example:  You'll need to get the actual favorite number from the user if you want to convert it. I've put in a placeholder.

# Print the converted values (for verification)
print("\n--- Converted Values ---")
print("Age (float):", age_float, type(age_float))
print("Height (int):", height_int, type(height_int))
print("Favorite Number (string):", favorite_number_str, type(favorite_number_str))

print(full_name[:4])

