#!/usr/local/bin/python3

A = [0,1,2,3,4,5]

for x in A:
    if x == 3:
        break     # breaks the loop
    print(x)

print('-----------------------')
for x in A:
    if x == 3:
        continue  # when condition is matched, returns to the iteration
    print(x)
    print('this should not be printed when x == 3')