import time
from multiprocessing import Process, Value, Array, Lock, Pool
import os


# def add_100(number: Value, lock: Lock):
#         for i in range(100):
#             time.sleep(.01)
#             with lock:
#                 number.value += 1
# Shared value with lock
# if __name__ == "__main__":
#     shared_number = Value('i',0)
#     print("Number at start",shared_number.value)
#     lock = Lock()
#
#     p1 = Process(target=add_100, args=(shared_number,lock))
#     p2 = Process(target=add_100, args=(shared_number,lock))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print("Number at end",shared_number.value)

# def add_100(numbers: Array, lock: Lock):
#     for i in range(100):
#         time.sleep(.01)
#         for i in range(len(numbers)):
#             with lock:
#                 numbers[i] += 1
#
# # Shared Array
# if __name__ == "__main__":
#     shared_array = Array('d',[0.0, 100.0, 200.0])
#     print("Value at start",shared_array[:])
#     lock = Lock()
#
#     p1 = Process(target=add_100, args=(shared_array,lock))
#     p2 = Process(target=add_100, args=(shared_array,lock))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print("Number at end",shared_array[:])

# Pools

def cube(number):
    return number ** 3

if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()

    result = pool.map(cube,numbers)

    pool.close()

    pool.join()

    print(result)