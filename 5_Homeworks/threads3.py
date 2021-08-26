import os
import threading
import sys

def worker():
    return

count = int(input("Enter number of threads to start: "))
threads = int(count)

thread = []
locks = []

print("\nMain process has pid of: ", os.getpid())
for i in range(threads):
    t = threading.Thread(target = worker)
    thread.append(t)
    locks.append(os.fork)
    t.start()
    print("Thread #: ", str(i))
    x = os.popen('whoami').read()
    print("User running: ", str(x))
    locks[i] = os.fork()
    if locks[i] == 0:
        print()
        exit()
    pass
    finished = os.wait(0, 0)
    print("ID of new child is: ", str(finished[0]))
    
