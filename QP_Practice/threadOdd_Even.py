import threading
def printEven() :
    for i in range(1,10) :
        if i % 2 == 0 :
            print(i)
    
    
def printOdd() :
     for i in range(1,8) :
        
        if i % 2 != 0 :
            print(i)
            
evenThread = threading.Thread(target=printEven)
oddThread = threading.Thread(target=printOdd)

evenThread.start()
oddThread.start()

evenThread.join()
oddThread.join()
