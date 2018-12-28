## lists

# set an print a list
x = [5,1,3,7,643,908]
print(x)

# print index 0 (first position of the index)
print("the index zero for the list is = ", x[0])
print("the index two for the list is = ", x[2])

# nested lists
y = ['a','b','z',[2,4,6,7],'potato','apple']
print("the index zero for the list is =", y[4])
print("this index position contains another list", y[3])

# insert value on a existing index position
print("original list members =", x)
x.insert(1,9999)
print("updated list =", x)

# append values
print("original list members =", x)
x.append(84757)
print("APPEND updated list =", x)

# remove value on a existing idex position
print("original list members =", x)
x.remove(9999)
print("REMOVE updated list: ", x)

# remove the last index for a list
print("original list members =", x)
x.pop()
print("REMOVE LAST INDEX updated list: ", x)

# sort list
print("not ordered list: ", x)
x.sort()
print("incremental sort list: ", x)
x.reverse()
print("reverse sort list: ", x)

# copy list
z = x.copy()
print("this is a new brand list copied from existing one: ", z)

# delete list (should drop an error "NameError: name y is not defined)
print(y)
del y
print(y)

# clear existing list
print(x)
x.clear()
print(x)