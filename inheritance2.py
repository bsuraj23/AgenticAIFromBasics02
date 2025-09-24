# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   
        self.student_id = student_id

    def show_details(self):   
        super().show_details()
        print(f"Student ID: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_details(self):
        super().show_details()
        print(f"Subject: {self.subject}")


class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_topic):
        super().__init__(name, age, student_id)
        self.thesis_topic = thesis_topic

    def show_details(self):
        super().show_details()
        print(f"Thesis Topic: {self.thesis_topic}")


p1 = Person("Alice", 40)
p1.show_details()

print("\n--- Student ---")
s1 = Student("Bob", 20, "S123")
s1.show_details()

print("\n--- Teacher ---")
t1 = Teacher("Dr. Smith", 45, "Mathematics")
t1.show_details()

print("\n--- Graduate Student ---")
g1 = GraduateStudent("Charlie", 25, "G456", "Machine Learning in Healthcare")
g1.show_details()
