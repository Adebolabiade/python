x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 


#Result Size: 785 x 584
x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 



x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = ("apple", "banana", "cherry")

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = range(6)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# Create a float
my_float = 3.14159

# Convert float to integer (truncates decimal part)
my_int = int(my_float)
print("Float to integer:", my_int)  # Output: 3

# Create a string representing a float
my_string = "2.71828"

# Convert string to float
string_to_float = float(my_string)
print("String to float:", string_to_float)  # Output: 2.71828

# Create a list of numbers
my_list = [1, 2, 3, 4, 5]

# Convert list to tuple
my_tuple = tuple(my_list)
print("List to tuple:", my_tuple)  # Output: (1, 2, 3, 4, 5)
import datetime

def calculate_birth_year(age_str):
  """
  Calculates the birth year from the given age as a string.

  Args:
    age_str: The age of the person as a string.

  Returns:
    The birth year as an integer, or None if the input is invalid.
  """
  try:
    age = int(age_str)
    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    return birth_year
  except ValueError:
    print("Invalid input. Please enter a valid integer for age.")
    return None

if __name__ == "__main__":
  user_age = input("Enter your age: ")
  birth_year = calculate_birth_year(user_age)

  if birth_year is not None:
    print(f"You were born in {birth_year}.")