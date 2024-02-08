import _thread
import time
def task( threadName, delay):
   for count in range(1, 6):
      time.sleep(delay)
      print ("Thread name: {} Count: {}".format ( threadName, count ))

try:
   _thread.start_new_thread( task, ("Thread-1", 2, ) )
   _thread.start_new_thread( task, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while True:
   pass