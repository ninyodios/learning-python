#!/usr/local/bin/python3

# slice values from indicated position indexes

a = [0,1,2,3,4,5,6,7,8] # array
b = (0,1,2,3,4,5,6,7,8) # tuple
c = '012345678' # string

# prints starting index position 0 and stop at index position 5 (not included)
x = slice(0,5) 
print (a[x])

# other way
print (a[0:5])

# options
print (a[3:])  # [start:] item start 
print (a[:5])  # [:end] item stop (same as [0:5])
print (a[:])   # copy array
print (a[::2])  # print every n position (in this case, every 2 index positions)
print (a[0:4:2])  # [start:end:step]item range; print every n position (in this case, every 2 index positions)

# index example
# -------------------------
# | P | Y | T | H | O | N |
# -------------------------
# | 0 | 1 | 2 | 3 | 4 | 5 |
# |-6 |-5 |-4 |-3 |-2 |-1 |  # Negative index

print (a[0])   # prints first positive index; starting from left side
print (a[-1])  # prints first negative index; starting from right side

print (a[::-1]) # prints array in reverse order
print (a[:-3:-1]) # prints last 2 values

