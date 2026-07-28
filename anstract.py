# Program to demonstrate Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")

# Creating an object
my_car = Car()

# Calling the method
my_car.start()