class Student:
    school = "ABC College"

    # Constructor
    def __init__(self, name):
        self.name = name

    # Instance Method
    def display(self):
        print("Student Name:", self.name)

    # Class Method
    @classmethod
    def show_school(cls):
        print("School Name:", cls.school)

    # Static Method
    @staticmethod
    def welcome():
        print("Welcome to Python!")

# Creating an object
student1 = Student("Rahul")

# Calling the methods
student1.display()         # Instance Method
Student.show_school()      # Class Method
Student.welcome()          # Static Method