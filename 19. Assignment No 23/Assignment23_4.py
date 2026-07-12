"""4: Write a program that counts how many odd numbers exist between
1 and N."""

import multiprocessing
import os

def CountOdd(No):
    print(f"PID of CountOdd: {os.getpid()}, PPID of CountOdd: {os.getppid()}")

    Count = 0
    for i in range(1,No+1):
        if i % 2 !=0:
            Count += 1
    return Count

def main():
    print(f"PID of main: {os.getpid()}, PPID of main: {os.getppid()}")

    Data = [1000000, 2000000, 3000000, 4000000]

    Result =[]

    mp = multiprocessing.Pool()
    Result = mp.map(CountOdd,Data)

    mp.close()
    mp.join()

    print("Result:  ",Result)

if __name__ == "__main__":
    main()