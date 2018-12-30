#!/usr/local/bin/python3

# https://www.codewars.com/kata/alien-accent/train/python

def convert(st):
    st = (st.replace("o","u"))
    st = (st.replace("a","o"))
    return(print(st))

convert("hello")

def convert2(st):
    return(print(st.replace('o','u').replace('a','o')))

convert2("hello")
