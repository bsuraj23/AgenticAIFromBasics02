# How to delete Instance Variable from the Object
class Student:
    def __init__(self):
        self.name = "Tom"
s = Student()
del s.name
