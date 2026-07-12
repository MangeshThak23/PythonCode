"""2. Write a program that calculates factorials of multiple numbers
simultaneously using Pool.map()."""

import multiprocessing
import os

def Factorial(No):
    PID = os.getpid()
    print(f"Process ID factorial: {PID}")

    if No<0:
        return "Number is negative."
    Result = 1
    for i in range(1,No+1):
        Result *=i
    return Result

def main():
    Data = [10,15,20,25]
    
    Result = []
    
    P = multiprocessing.Pool()
    
    Result = P.map(Factorial,Data)
    
    P.close()
    P.join()

    print("-"*30)

    PID = os.getpid()
    print("Main PID:    ",PID)

    print(f"The input data: {Data}")
    print(f"The factorial:  {Result}")

if __name__ == "__main__":
    main()