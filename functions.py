def my_func():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(num1 + num2)
   
my_func()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")






def my_function(*kids):
  print("The youngest child is " + kids[2])#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

my_function("Emil", "Tobias", "Linus")




def my_function(**kid):
  print("His last name is " + kid["lname"])#If the number of keyword arguments is unknown, add a double ** before the parameter name:

my_function(fname = "Tobias", lname = "Refsnes")



def my_function(country = "Norway"):
  print("I am from " + country)#If we call the function without argument, it uses the default value:

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")














