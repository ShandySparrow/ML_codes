from concurrent.futures import ThreadPoolExecutor
from time import sleep
def square(numbers):
   for val in numbers:
      ret = val*val
      sleep(1)
      print("Number:{} Square:{}".format(val, ret))
def cube(numbers):
   for val in numbers:
      ret = val*val*val
      sleep(1)
      print("Number:{} Cube:{}".format(val, ret))
if __name__ == '__main__':
   numbers = [1,2,3,4,5]
   executor = ThreadPoolExecutor(2)
   thread1 = executor.submit(square, (numbers))
   thread2 = executor.submit(cube, (numbers))
   print("Thread 1 executed :",thread1.done())
   print("Thread 2 executed :",thread2.done())
   sleep(2)
   print("Thread 1 executed :",thread1.done())
   print("Thread 2 executed :",thread2.done())
