import threading
import time
def task():
    print("thread started")
    time.sleep(2)
    print("threading finished")
t1 = threading.Thread(target=task)
t1.start()
t1.join()
print("thread terminated")
