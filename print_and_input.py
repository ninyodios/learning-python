### Print

#%s string
#%d interger
#%f floating

x = 10
y = 50
z = 99.9500000

print(x + y)

print ("{0} + {1} = {2}".format(x, y, x + y))

print ("Hello", "world", sep="---")

name = "afro"
print ("hello %s" % name)
print ("hello %s, are you %d years old?" % (name, y))
print ("Success percentage is: %f " %z)
print ("Success percentage is: %.3f " %z)

### Input

value = input ("Insert some value:")
print (value) # this will return a string

#cast interger 
value = int (input ("Insert some value:"))
print (value)

#cast float
value = float (input ("Insert some value:"))
print (value)
