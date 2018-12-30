#!/usr/local/bin/python3

# Atom | To run the script, use CMD+I

def array_diff(a, b):
    b = set(b)
    print(list(item for item in a if item not in b))
    return(list(item for item in a if item not in b))

array_diff([1,2,2],[1] )  # shoult return [2,2]
