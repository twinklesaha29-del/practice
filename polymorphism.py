# Program to demonstrate Polymorphism

class Cat:
    def sound(self):
        print("Cat says: Meow")

class Dog:
    def sound(self):
        print("Dog says: Woof")

# Same method, different behavior
animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()