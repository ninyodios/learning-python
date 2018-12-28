
# In Python boolean values are two constant objects which are true and false.

x=10
y=11

print(x == y)
print(x != y)
print("result:", x == 10 and y == 13)
print("not result:", not x==y)

x="hello"
y="goodbye"

print(x == y)
print(x != y)


### from udemy track
#Boolean, Comparison Operators and Logical Operators in Python
# 
#>>> True
#True
#>>> False
#False
#>>> true
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#NameError: name 'true' is not defined
#>>> false
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#NameError: name 'false' is not defined
#>>> 10 > 9
#True
#>>> 10 < 9
#False
#>>> 100 == 100
#True
#>>> 100 == 99
#False
#>>> 100 != 99
#True
#>>> x = 20
#>>> y = 30
#>>> x >= y
#False
#>>> x = 30
#>>> x <= y
#True
#>>> 'hello' == "hello"
#True
#>>> 'hello'.isupper()
#False
#>>> 'hello'.islower()
#True
#>>> 'hello'.isalpha()
#True
#>>> 'hello'.isalnum()
#True
#>>> 10 > 9 and 20 < 15
#False
#>>> 10 > 9 or 20 < 15
#True
#>>> 10 > 9 or 20 > 15
#True
#>>> not 10 > 9
#False
#>>> not 10 < 9
#True
