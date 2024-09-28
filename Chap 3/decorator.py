# decorator is a powerfull tool which is used to modify the behaviour of the function as well as it is used to solve complex problems

# def example_decorator(func) :
#     something

# def example_function() :
#     something
#     something

# @example_decorator(example_function)

# def message_decorator(func) :
#     def add() :
#         n1 = 10;
#         n2 = 20;
#         n3 = n1 + n2
#         print("addition is :",n3)
#     func()
#     print("welcome to decorator!")
#     return add()
# def msg() :
#     print("hello!")

# xdecor =  message_decorator(msg)

import time
import math

def caltime(func) :
    def inner_function(*args) :
        begins = time.time()
        print("hello")
        func(*args)
        end = time.time()
        print("total time = ",end-begins)
    return inner_function
@caltime

def factorial(n) :
    time.sleep(2)
    print("factorial of number :",math.factorial(n))
factorial(5)



