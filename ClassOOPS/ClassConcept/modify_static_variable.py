# Where we can modify the Value of Static Variable
class Student:
    school = "ABC School"
    def change_school(self, new_name):
        Student.school = new_name
