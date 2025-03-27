# Diamond Pattern
n = 5  # Number of rows

# Upper part of the diamond
for i in range(n):  # Loop through rows from 0 to n-1
    spaces = ' ' * (n - i - 1) # Calculate the number of spaces before the asterisks
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Lower part of the diamond
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    
    
    
def print_pattern(n):
    #Prints the given pattern with n rows in the upper part.

    # Upper part of the pattern
    for i in range(1, n + 1):
        print('* ' * i)  # Print '*' i times, with a space after each

    # Lower part of the pattern
    for i in range(n - 1, 0, -1):
        print('* ' * i)  # Print '*' i times, with a space after each

# Example usage with n = 5
print_pattern(5)


name = "Habeeb"

reversed_name = name[::-1]# the double colon has the effect of reversing the string it goes back form the specified position e.g

print (reversed_name)
