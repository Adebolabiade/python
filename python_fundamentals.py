# Step 1: Program Introduction
print("Welcome to the Personalised User Profile Generator!")
print("This program collects and processes user information.")  # Explains the program's purpose

# Step 2: Collecting & Processing User Input
full_name = input("Enter your full name: ")  # String input
age = int(input("Enter your age: "))  # Convert input to integer
height = float(input("Enter your height in cm: "))  # Convert input to float
fav_lang = input("Enter your favourite programming language: ")  # String input
fav_number = int(input("Enter your favourite number: "))  # Convert input to integer
description = input("Describe yourself in a few words: ")  # String input

# Data type conversions
age = float(age)  # Convert age to float
height = int(height)  # Convert height to integer
fav_number = str(fav_number)  # Convert favourite number to string

# Step 3: String Manipulation & Formatting
first_name = full_name.split()[0]  # Extract first name
upper_first_name = first_name.upper()  # Convert first name to uppercase
name_length = len(full_name)  # Find the length of full name

# Replace "Python" if chosen
if fav_lang.lower() == "python":
    fav_lang = "a powerful language"

# Display formatted information
print(f"\nHello {upper_first_name}!")
print(f"Your full name has {name_length} characters.")
print(f"Your favourite programming language is {fav_lang}!")

# Step 4: Performing Calculations & Conditional Logic
current_year = 2025  # Assume current year is 2025
year_turn_100 = current_year + (100 - int(age))  # Calculate year they turn 100
age_sum = int(age) + int(fav_number)  # Sum of age and favourite number

print(f"You will turn 100 in the year {year_turn_100}.")
print(f"Your age plus your favourite number equals {age_sum}.")

# Age-based conditional statement
if int(age) >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Step 5: Output & Summary
print("\n--- User Profile Summary ---")
print(f"Full Name: {full_name}")
print(f"Age: {age} years old")
print(f"Height: {height} cm")
print(f"Favourite Programming Language: {fav_lang}")
print(f"Favourite Number: {fav_number}")
print(f"About You: {description}")

# Challenge: Name Reversal & Letter Separation
reversed_name = full_name[::-1]  # Reverse the full name
spaced_name = " ".join(full_name)  # Add spaces between letters

print(f"\nYour name in reverse: {reversed_name}")
print(f"Your name with spaced letters: {spaced_name}")
