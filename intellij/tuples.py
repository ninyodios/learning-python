## tuples
# tuples are like lists, but they are inmutable

x = (2,4,78,937,1038)
print(x)

# print index zero element
print(x[0])

# join x and y tuples
y = (6,'potato',8.9,875758)
z = x + y
print("this is a new tuple= ", z)

# something weird. create a tuple with the provided value multiplied by
a = ('repeatMe',) * 10
print(a)
