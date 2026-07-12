"""3: Write a program that counts how many even numbers exist
between 1 and N using Pool.map()."""

import multiprocessing
import os

def CountEven(No):
    print(f"PID of CountEven: {os.getpid()}, PPID of CountEven: {os.getppid()}")
    Count = 0
    for i in range(1,No+1):
        if i % 2 == 0:
            Count += 1
    return Count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []
    print(f"PID of main: {os.getpid()}, PPID of main: {os.getppid()}")

    mp = multiprocessing.Pool()
    Result = mp.map(CountEven, Data)

    mp.close()
    mp.join()

    print("Result: ",Result)

if __name__ == "__main__":
    main()