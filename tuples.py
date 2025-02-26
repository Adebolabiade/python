x = ("apple", "banana", "cherry")#updating tuples
y = list(x)#tuples need to be converted to a list to be altered
y[1] = "kiwi"
x = tuple(y)# assign a new variable a list format of the tuple

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)#tuple needs to be converted to a list
y.append("orange")#applywhatever changes you want
thistuple = tuple(y)#restablish that the list form of the x or y was originally a tuple 

print(thistuple)


fruits = ("apple", "banana", "cherry")#pack the tuple

(green, yellow, red) = fruits# the sum of the items in the tuple is equal to the variable

print(green)#green in its order represent apple
print(yellow)#followed by yellow which represents banana
print(red)#and red which repreents cherry

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits#the asterisks assigns the rest of the objects to red
print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits#in this case tropic only represents the 3 centre fruits because of the position of red and cherry (last place)

print(green)
print(tropic)
print(red)





