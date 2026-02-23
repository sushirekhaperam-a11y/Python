import threading
import time
def download_file(filename):
    print(("Downloading file"))
    time.sleep(2)
    print(f"{filename} downloaded")
files = ["file1.txt","file2.txt","file3.txt"]
threads = [threading.Thread(target=download_file,args=(file,)) for file in files]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()