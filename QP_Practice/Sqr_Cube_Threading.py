import threading

def findSquare(num) :
    sqr = num * num
    print(f"square of {num} is {sqr}")
    
def findCube(num) :
    cube = num ** 3
    print(f"cube of {num} is {cube}")
    

def main() :
    number = 5
    square_thread = threading.Thread(target=findSquare, args=(number,))
    cube_thread = threading.Thread(target=findCube,args=(number,))
    
    square_thread.start()
    cube_thread.start()
    
    square_thread.join()
    cube_thread.join()
    
    
main()

# pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$*])[a-zA-Z\d@#$*]{8,20}$"
urlPattern = r"^"
    
    