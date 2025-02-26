a = 200
b = 33

#booleans or bool in python define /hold onr or two values either true or false its just a term that represents true or false
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The following code will result i true
print(bool("Hello"))
print(bool(15))

#The below operations will result in false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Booleans can alsow be used with functions e.g  
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  x = 200
print(isinstance(x, int))

