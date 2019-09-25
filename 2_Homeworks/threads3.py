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