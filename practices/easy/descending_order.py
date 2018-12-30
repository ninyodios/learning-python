#!/usr/local/bin/python3

# https://www.codewars.com/kata/descending-order/train/python

def Descending_Order(num):
    X = str(num)
    Y = list(map(int, X))
    Z = sorted(Y, reverse=True)
    R = ''.join(map(str, Z))
    return int(R)
    #return print(int(R))

Descending_Order(987654321)
