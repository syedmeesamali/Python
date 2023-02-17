import os
import threading

def task1():
    print("Task 1 assigned to thread:{}".format(threading.current_thread().name))
    print("ID of task-1 is: {}".format(os.getpid()))

def task2():
    print("\nTask 2 assigned to thread:{}".format(threading.current_thread().name))
    print("\nID of task-2 is: {}".format(os.getpid()))

if __name__ == "__main__":
    print("ID of running main thread: {}".format(os.getpid()))
    print("Name of main thread is:{}".format(threading.current_thread().name))
    t1 = threading.Thread(target=task1, name="t1")
    t2 = threading.Thread(target=task2, name="t2")
    t1.start()
    t2.start()
