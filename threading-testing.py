from threading import Thread, Lock, current_thread
from queue import Queue
import time

# Threading with locks
#database_val = 0

# def increase(lock):
#     global database_val
#
#     with lock:
#         local_db = database_val
#         # processing
#         local_db += 1
#         time.sleep(.1)
#         database_val = local_db

def worker(queue: Queue, lock: Lock):
    while True:
        value = queue.get()

        # processing
        with lock:
            print(f"In {current_thread().name} got {value}")
        queue.task_done()

if __name__ == "__main__":
    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True
        thread.start()


    for i in range(1,21):
        q.put(i)

    q.join()


    print("End main")