import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_process():
    while True:
        with lock1:
            with lock2:
                print("hi")
                pass

def thread2_process():
    while True:
        with lock2:
            with lock1:
                print("bye")
                pass

thread1 = threading.Thread(target=thread1_process)
thread2 = threading.Thread(target=thread2_process)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
