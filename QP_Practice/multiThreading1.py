import threading

def printSqrOfOdd(list1) :
    print("printing square of odd number :")
    sqaure = lambda x : x * x
    for i in list1 :
        if i % 2 != 0 :
            print(sqaure(i))

def printCubeEven(list1) :
    print("printing cube of even number :")
    cube = lambda x : x ** 3
    for i in list1 :
        if i % 2 == 0 :
            print(cube(i))
    
    
    
list1 = []
for _ in range(10) :
    number = int(input(f"enter num{_+1} :"))
    list1.append(number)


def main() :
    sqrOdd = threading.Thread(target=printSqrOfOdd,args=(list1,))
    cubeEven = threading.Thread(target=printCubeEven,args=(list1,))
    
    sqrOdd.start()
    cubeEven.start()
    
    sqrOdd.join()
    cubeEven.join()
    
main()