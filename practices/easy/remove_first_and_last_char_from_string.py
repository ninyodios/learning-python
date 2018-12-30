#!/usr/local/bin/python3

# Atom | To run the script, use CMD+I

def remove_char(s):
    print(s[1:-1:])
    r = s[1:-1:]
    return str(r)

remove_char("potato")

# More elegant
def remove_char(s):
    return s[1:-1:]

remove_char("apple")
