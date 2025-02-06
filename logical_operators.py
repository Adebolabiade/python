print(10//3)

 #Check if a number is divisible by both 3 and 5
def is_divisible_by_3_and_5(number):
    
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

# Get input from the user
num = int(input("Enter a number: "))

# Check and print the result
if is_divisible_by_3_and_5(num):
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")



 #What will print(5 & 3) output?

print(5 & 3) 