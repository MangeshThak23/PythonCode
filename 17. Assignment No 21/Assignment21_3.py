"""3: Design a Python application where multiple threads update a shared variable.
• Use a Lock to avoid race conditions.
• Each thread should increment the shared counter multiple times.
• Display the final value of the counter after all threads complete execution."""

import threading

counter = 0
lock = threading.Lock()

def incrementnmber():
    global counter
    for i in range(300000):
        lock.acquire()
        counter += 1
        lock.release()

def main():

    t1 = threading.Thread(target=incrementnmber)
    t2 = threading.Thread(target=incrementnmber)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(counter)


if __name__ == "__main__":
    main()
    