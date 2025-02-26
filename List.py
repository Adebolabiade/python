thislist1st = ["apple", "banana", "cherry"]
print(thislist1st[1])


thislist2nd = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2nd[1:3] = ["blackcurrant", "watermelon"]
print(thislist2nd)


thislist3rd = ["apple", "banana", "cherry"]
thislist3rd[1] = "blackcurrant"
print(thislist3rd)


thislist4th = ["apple", "banana", "cherry"]
thislist4th.append("orange")
print(thislist4th)

thislist5th = ["apple", "banana", "cherry"]
thislist5th.remove("banana")
print(thislist5th)


thislist6th = ["apple", "banana", "cherry"]
for x in thislist6th:
  print(x)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)





