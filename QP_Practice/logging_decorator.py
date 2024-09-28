def logging_decorator(func) :
    def wrapper(*args, **kwargs) :
        print(f"calling function with arguments : {args},{kwargs}")
        result = func(*args, **kwargs)
        print(f"function name :{func.__name__} returned : {result}")
        return result
    return wrapper

@logging_decorator
def add(x,y) :
    return x + y

@logging_decorator
def mul(x,y) :
    return x * y
add(10,20)
mul(5,10)