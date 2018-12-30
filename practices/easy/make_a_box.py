#!/usr/local/bin/python3

#https://www.codewars.com/kata/make-a-square-box/train/python

def box(n):
    closers = '-' * n
    edge = '-' + (' '*(n-2)) +'-'
    return [closers]+[edge for i in range(n-2)]+[closers]

print(box(9))
