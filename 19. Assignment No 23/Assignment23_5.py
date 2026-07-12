"""5: Write a program that calculates factorials of multiple numbers
simultaneously using multiprocessing.Pool."""

import multiprocessing
import os

def Factorial(No):
    print(f"PID of Factorial: {os.getpid()}, PPID of Factorial: {os.getppid()}")
    Result = 1
    for i in range(1,No+1):
        Result *= i
    print(f"Factorial:{Result}")
    print("-"*45)

def main():
    print(f"PID of main: {os.getpid()}, PPID of main: {os.getppid()}")
    print("-"*45)

    Data = [10, 15, 20, 25]

    mp = multiprocessing.Pool()
    Result = mp.map(Factorial,Data)

    mp.close()
    mp.join()

    #print("Result:  ",Result)

if __name__ == "__main__":
    main()

