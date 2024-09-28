try :
    num = int(input("enter a integer number :"))
    print("you have entered :",num)
except ValueError as e :
    print("you have entered floating point instead of integer")