"""3. For every number in the given list, count how many prime numbers
exist between 1 and N using multiprocessing Pool."""

import multiprocessing

def PrimeNum(No):
    if No<=1:
        return False
    
    if No == 2:
        return True
    
    if No % 2 == 0:
        return False
    

    i = 3
    while i**2 <= No:
        if No % i == 0:
            return False
        i += 2
    return True


def CountPrimees(No):
    if No<1:
        print("Invalid number.")
        return 0
    Count = 0

    for i in range(1,No+1):
        if PrimeNum(i):
            Count += 1
    return Count


def main():
    Data = [10000,20000,30000,40000]
        
    P = multiprocessing.Pool()
    Result = P.map(CountPrimees,Data)

    P.close()
    P.join()
    print("Total prime count for each number:",Result)

if __name__ == "__main__":
    main()


