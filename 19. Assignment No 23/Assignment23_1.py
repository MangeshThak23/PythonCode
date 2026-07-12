"""1: Write a Python program using multiprocessing.Pool to calculate the
sum of all even numbers from 1 to N for every number from the given
list."""

import os
import multiprocessing

def SumEven(No):
    print(f"PID of SumEven is: {os.getpid()}, PPID of SumEven is: {os.getppid()}")

    Sum = 0
    for i in range(2,No+1,2):
        Sum = Sum + i
    return Sum

def main():
    print(f"PID of main is: {os.getpid()}, PPID of main is: {os.getppid()}")
    
    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []
    
    mp = multiprocessing.Pool()
    
    Result = mp.map(SumEven,Data)
    

    mp.close()
    mp.join()

    print("The result is:",Result)

if __name__ == "__main__":
    main()
