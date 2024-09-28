# from scipy.optimize import linprog

# # Define the objective function
# c = [3, 5, 4]

# # Define the constraints
# A = [[2, 3, 0], [0, 2, 5], [3, 2, 4]]
# b = [8, 10, 15]

# # Define bounds for variables (all non-negative)
# bounds = ((0, None), (0, None), (0, None))

# # Solve the linear programming problem
# res = linprog(c, A_eq=A, b_eq=b, bounds=bounds)

# # Print the solution
# print("Optimal solution:", res.x)
# print("Optimal objective value:", res.fun)

# def infinite_num() :
#     i = 1
#     while True :
#         yield i
#         i+=1
        
# result = infinite_num()
# print(type(result))
# for num in infinite_num() :
#     if num > 10 :
#         break
#     print(num)

# # printing even numbers by using generators
# def even_num(range) :
#     num = 1
#     while num <= range :
#         if num % 2 == 0 :
#             yield f"{num}"
#         # else :
#         #     yield f"odd :{num}"
#         num += 1;
        
# result = even_num(10)
# for even in even_num(10) :
#     print(even)    

# decorators 

def logging_decorator(func) :
    def wrapper(*args,**kwargs) :
        print(f"calling function : {func.__name__}")
        result = func(*args,**kwargs)
        print(f"function result : {result}")
        return result;
    return wrapper;
                                                
@logging_decorator
def add(x,y) :
    return x + y

result = add(3,5)
print(result)