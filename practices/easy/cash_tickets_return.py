#!/usr/local/bin/python3

# https://www.codewars.com/kata/vasya-clerk/train/python

def tickets(people):
    n25, n50, n100, cash = 0, 0, 0, 0
    cash_return = 'YES'

    for cash in people:
        if cash == 25:
            n25 += 1
        elif cash == 50 and n25 > 0:
            n50 += 1
            n25 -= 1
        elif cash == 100:
            if n50 > 0 and n25 > 0:
                n25 -= 1
                n50 -= 1
                n100 += 1
            elif n50 == 0 and n25 >= 3:
                n25 -= 3
                n100 += 1
            else:
                cash_return = 'NO'
        else:
            cash_return = 'NO'
    return(print(cash_return))
    return cash_return

tickets([25,25,50,100,25])
