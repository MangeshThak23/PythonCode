"""4. Write a program that calculates
1^5+2^5+3^5+.....+N^5
for multiple values of N simultaneously using Pool.
Input

[1000000,
2000000,
3000000,
4000000]
Measure total execution time."""

import os
import time
import multiprocessing

def Calculation(No):
    print(f"PID of calculation: {os.getpid()}, PPID of calculation: {os.getppid()}")
    Sum = 0
    for i in range(1,No+1):
        Sum = i**5 + Sum
    return Sum

def main():
    print(f"PID of main: {os.getpid()}, PPID of main: {os.getppid()}")

    Data = [1000000,2000000,3000000,4000000]

    start_time = time.perf_counter()
    
    mp = multiprocessing.Pool()
    Result = mp.map(Calculation,Data)

    mp.close()
    mp.join()

    print(f"Result is: {Result}")

    end_time = time.perf_counter()
   
    print(f"Time required is: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()



