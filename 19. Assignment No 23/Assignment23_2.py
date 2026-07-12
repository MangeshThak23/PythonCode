"""2: Write a Python program using multiprocessing.Pool to calculate the
sum of all odd numbers from 1 to N."""

import multiprocessing
import os

def SumOdd(No):
    print(f"The PID of SumOdd is: {os.getpid()}, PPID of SumOdd is: {os.getppid()}")

    Sum = 0
    for i in range(1,No+1,2):
        Sum = Sum + i
    return Sum

def main():
    print(f"PID of main: {os.getpid()}, PPID of main: {os.getppid()}")

    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []

    mp = multiprocessing.Pool()
    Result = mp.map(SumOdd,Data)

    mp.close()
    mp.join()

    print("Result is:   ",Result)

if __name__ == "__main__":
    main()