#!/usr/local/bin/python3

# https://www.codewars.com/kata/exes-and-ohs/train/python

#XO("ooxx") => true
#XO("xooxx") => false
#XO("ooxXm") => true
#XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
#XO("zzoo") => false
# return boolean
# case insensitive
# string can contain any char
# check if a string has the same amount of 'x's and 'o's.

def xo(s):
    s = s.lower()
    x = (s.count("x"))
    o = (s.count("o"))
    if x == o:
        return True
        #return print(bool(True))
    else:
        return False
        #return print(bool(False))

xo("potatOXx")

# simple
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

xo("pOtatOXx")
