# Nested Functions
def outer():
    def inner():
        print("Inside inner function")
    inner()
outer()
