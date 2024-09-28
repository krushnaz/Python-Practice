import threading 

share_resource = 0
lock = threading.Lock()
def increment() :
    global share_resource
    for _ in range(10000) :
        lock.acquire()
        share_resource +=1
        lock.release()
        
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)
print("thread -1")
thread1.start()
print("thread -2")
thread2.start()

thread1.join()
thread2.join()
print(share_resource)
print("end...")