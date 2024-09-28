# def msg() :
#     print("welcome!");
    
# msg()

# call by value :
# we pass the value of the parameter during calling of the function 
# list1 = [1,2,3,4,5];
# print("first list :",list1);
# def changeList(list1) :
#     # list1 = [10,20,30,40,50];
#     list1.append([10,20,30,40,50])
#     print("inside :",list1);
#     return;

# l = [100,200,300,400,500];
# changeList(l);

# perfrom arthimatic operation using function

# def addition(a,b) :
#     return a + b;
# def subtraction(a,b) :
#     return a - b;
# def multiplication(a,b) :
#     return a * b;
# def division(a,b) :
#     return b/a;

# print( "addition :",addition(10,20));
# print( "subtraction :",subtraction(10,20));
# print( "multiplication :",multiplication(10,20));
# print( "division :",division(10,20));

# function which does not takes argument and does not return value 
# count characters from the string 

# def countA() :
#     str = input("enter a string :");
#     count = str.count("a");
#     print("number of a in string are :",count);
# countA();

# take argument does not return value 
# def countA(str) :
#     # str = input("enter a string :");
#     count = str.count("a");
#     print("number of a in string are :",count);

# str = input("enter a string :");
# countA(str);

# taking argument and returning value

def countA(str) :
    # str = input("enter a string :");
    count = str.count("a");
    return count;
str = input("enter a string :");
print("number of a in string are :",countA(str));
