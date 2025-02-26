def is_valid_age(age):
    """
    Checks if an age is valid (between 18 and 65 inclusive).

    Args:
        age: The age to check (an integer).

    Returns:
        True if the age is valid, False otherwise.
    """

    try:  # Try to convert user input to an integer
        age = int(age)  # Cast to integer if it's a string or float

        if 18 <= age <= 65:
            return True
        else:
            return False

    except ValueError:  # Handle cases where the user input is not a valid number
        return False  # Return False if age cannot be converted to int


# Get user input and test the function
user_age = input("Enter your age: ")

if is_valid_age(user_age):
    print("Valid age.")
else:
    print("Invalid age.")
