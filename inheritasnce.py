# Program to demonstrate Inheritance

class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):   # Dog inherits from Animal
    def bark(self):
        print("Dog says: Woof! Woof!")

# Creating an object of Dog
dog1 = Dog()

# Calling methods
dog1.sound()   # Inherited method
dog1.bark()    # Child class method