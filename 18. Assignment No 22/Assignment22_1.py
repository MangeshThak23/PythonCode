"""1. Write a program that accepts a list of integers and uses Pool.map()
to calculate the sum of squares from 1 to N for every element in the
list."""


import multiprocessing
import os

def SumSquare(No):
    print("PID is:  ",os.getpid())
    Sum = 0
    for i in range(1,No):
        Sum = Sum + (i**2)
    return Sum

def main():
    Data = [1000000,2000000,3000000,4000000]
    Result = []
    P = multiprocessing.Pool()
    Result = P.map(SumSquare,Data)
    P.close()
    P.join()
    print("-"*50)
    print(Result)
    
if __name__ == "__main__":
    main()
