# Concepts
Python or general coding concepts

## Object Oriented programming (OOP)
From wikipedia:
> "Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which may contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods. A feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated (objects have a notion of "this" or "self")"

- is centered in creating objects
- objects may interchange data 
- object:
  - instance of a classzoo
  - a single software unit that combines data and methods
    - data in a object are known as attributes
    - functions (or procedures) in an object are known as methods

Example of code for get a cab:
``` 
class Cab{
    cabService, make,location,numberPlate  # data
    book(), arrival(), start()             # methods
}

class CabDriver{
    name, employeeId        # data
    openDoor(), drive()     # methods
}

class passenger{
    name, address                  # data
    openApp(), bookCab(), walk()   # methods
}

