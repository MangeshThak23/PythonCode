"""5.Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. List contains the numbers 
which are accepted from user. 
Filter should filter out all prime numbers. Map function will multiply each number by 2.
Reduce will return Maximum number from that numbers. 
(You can also use normal functions instead of lambda functions)."""

from functools import reduce


def PrimeNum(No):
    if No<1:
        return False
    for i in range(2,No):
        if No % i == 0:
            return False
    return True

Mult = lambda No : No * 2

MaxNum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Mylist = []

    Num = int(input("Enter how much elements you want to enter in the list:  "))

    for i in range(Num):
        Elements = int(input("Enter the elements:   "))
        Mylist.append(Elements)
    print("The entered list is: ",Mylist)

    FData = list(filter(PrimeNum,Mylist))
    print("Prime numbers:   ",FData)

    MData = list(map(Mult, FData))
    print("After multiplication by 2:   ",MData)

    RData = reduce(MaxNum,MData)
    print("The maximum number from the list is: ",RData)

if __name__ == "__main__":
    main()

