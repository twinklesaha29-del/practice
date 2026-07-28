# Program to demonstrate Class, Object, and Constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


# Creating an object
student1 = Student("Rahul", 20)

# Calling the method
student1.show_details()