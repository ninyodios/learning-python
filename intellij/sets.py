## sets
# So a set is an unordered collection that no duplicate elements and no indexing.
# a set has unique values
# when a set is printed, it only print unique values, do not show duplicate values

# define and print set
x = {3,3,3,3,5,5,5,7,8,9,1,2,3,8}
print(x)

# another way to create a set
y = set(('potatos','chips','vegetables',4,8))
print(y)

# add item to set
x.add(99)
print(x)

# add multiple values to set
x.update([4,123,38477])
print(x)

# remove value from set
x.remove(123)
print(x)

# union set
print(x.union(y))
print(x|y)

# values on both sets (coincidences)
print(x.intersection(y))
print(x & y)

# diferences between x and y
print(x.difference(y))
# diferences between y and x
print(y - x)

# simetric difference (values from both sets that are not present in both)
print(x.symmetric_difference(y))
print(x ^ y)
# prints same values, different order (not relevant)
print(y.symmetric_difference(x))
print(y ^ x)