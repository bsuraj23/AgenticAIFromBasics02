# How to Access Instance Variables
class Student:
    def __init__(self, name):
        self.name = name
s = Student("Bob")
print(s.name)
