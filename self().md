

self (argument)
=================
In Python, self is a widely followed convention for naming the first argument in instance methods within a class. It represents the instance on which the method is being called, allowing access to instance attributes and methods.

Note: Although you can technically name this argument anything, using self is a strongly recommended convention. This makes your code more readable and familiar to other Python programmers.

self in Python class
======================
In Python, self is a fundamental concept when working with object-oriented programming (OOP). It represents the instance of the class being used. Whenever we create an object from a class, self refers to the current object instance. It is essential for accessing attributes and methods within the class.

Example:
class Mynumber:
    def __init__(self, value):
        self.value = value
    
    def print_value(self):
        print(self.value)
​
obj1 = Mynumber(17)
obj1.print_value()


The Role of "self" in Constructors and Methods
================================================
Self in the Constructor (__init__ method)

__init__ method is called when a new instance of the class is created. This method serves as the constructor for the class and initializes the object's attributes. The first argument of the __init__ method must always be self, as it allows the method to set instance attributes for the object being created.

Example:
class Subject:
​
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2
​
​
obj = Subject('Maths', 'Science')
print(obj.attr1)  
print(obj.attr2)

Explanation: In this example, self.attr1 and self.attr2 refer to the attributes of the current object, ensuring that each object can have its own values for these attributes.
    