# A) Write a program to demonstrate Decorators in Python
def uppercase_decorator(func) :
    def wrapper(*args, **kwargs) :
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name) :
    return f"good morning, {name}"

print(greet("krushna"))

    