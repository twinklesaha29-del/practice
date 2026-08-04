def outer():
    message = "Holaa!"

    def inner():
        print(message)   # Accesses variable from outer function

    return inner

greet = outer()
greet()