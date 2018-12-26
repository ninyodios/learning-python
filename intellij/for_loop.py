#!/usr/local/bin/python3

A = [0,1,2,3,4,5,6,7,8] # list
B = (0,1,2,3,4,5,6,7,8) # tuple
C = {0,1,2,3,4,5,6,7,8} # set
D = '012345678'         # string
E = {                   # dictionary
   "name": 'beto',
   "age": '41'
}

print(0 in A) # prints 'true' because 0 is present in A 
print("name" in E)  # prints 'true' because name is present in E
print(100 in A)     # prints 'false' because 100 is NOT present in

# will print all the items on the list
for x in A:
    print(x)

# for dictionaries
for x in E.keys():    # prints only keys
    print(x)
for x in E.values():  # prints only values
    print(x)
for key, value in E.items():  # prints key/value
    print(key,':',value)

for x in range(6):        # prints from 0 to 5
    print(x)
for x in range(2,20,5):   # (start,stop,step) (from 2, to 20, every 5)
    print(x)

