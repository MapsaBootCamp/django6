# Python program to illustrate the concept
# of threading
# importing the threading module
import time
import threading
import datetime
  
def print_cube(num):
    """
    function to print cube of given num
    """
    print("in cube.")
    time.sleep(30)
    print("Cube: {}".format(num * num * num))
    with open("log_cube.txt", "w") as f:
        f.write("helllllo cube")
  
def print_square(num):
    """
    function to print square of given num
    """
    print("in square.")
    time.sleep(20)
    print("Square: {}".format(num * num))
    with open("log_square.txt", "w") as f:
        f.write("helllllo square")
  
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,), daemon=False)
    t2 = threading.Thread(target=print_cube, args=(10,), daemon=True)
  
    # starting thread 1
    t1.start()
    # # starting thread 2
    t2.start()
    
    old_now = datetime.datetime.now()
    # # wait until thread 1 is completely executed
    # t1.join()


    # # wait until thread 2 is completely executed
    # t2.join()
    # both threads completely executed
    print("Done!")
    new_now = datetime.datetime.now()
    print(new_now - old_now)