perfect_day=("Wake up","Breakfast","Explore","Relax","Sleep")

print(perfect_day[0])#print index 0 or wake up

print(perfect_day[-1])#print sleep

print(perfect_day[1:4])#print centre 3

(a,b,c,d,e)=perfect_day#unpacking
print(a)
print(b)
print(c)
print(d)
print(e)

x=list(perfect_day)#conversion
x[1]=("lunch")#altering index 1
perfect_day=tuple(x)
print(x)


extras=("Read","Exercise")

full_day=("relax", "explore")

savvy = perfect_day+full_day#adding variables
print(savvy)

y=perfect_day.count("lunch")#number of times lunch was typed
print(y)

print(full_day.index("explore"))#index of explore

total_songs=len(full_day)#finding the total number of activities
print("total number of activities:", {total_songs})

a=list(full_day)#converting full_day to a list
print(a)


