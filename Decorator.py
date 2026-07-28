# Program to demonstrate a Decorator

def greet_message(func):
    def wrapper():
        print("Welcome!")
        func()
        print("Have a nice day!")
    return wrapper

@greet_message
def greet():
    print("Hello, Rahul!")

greet()