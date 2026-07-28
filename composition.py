# Program to demonstrate Composition

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car has an Engine

    def drive(self):
        self.engine.start()
        print("Car is moving.")

# Creating an object
my_car = Car()
my_car.drive()