#!/usr/local/bin/python3

# group of statements within a program that performs a specific task

#def name_of_function (arg1, arg2, arg3):
#    do_stuff

# suma function
def basic_sum(arg1, arg2):
    print(arg1 + arg2)

basic_sum(1,3)

# ensure args are same data type
def basic_sum(arg1, arg2):
    if type(arg1) != type(arg2):
        print("Args should be of the same type")
        return           #when case matches, it will finish here
    print(arg1 + arg2)

basic_sum(3, "patata")       # should fail as data types are different
basic_sum(3,5)               # should work
basic_sum("hello ", "world") # should work