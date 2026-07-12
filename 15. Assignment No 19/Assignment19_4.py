"""4.Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. List contains the numbers 
which are accepted from user. 
Filter should filter out all such numbers which are even. 
Map function will calculate its square.
Reduce will return addition of all that numbers."""

from functools import reduce

EvenData = lambda No : No % 2 == 0
SquareData = lambda No : No ** 2
AddData = lambda No1, No2 : No1 + No2

def main():
    Mylist = []

    Num = int(input("Enter how much elements you want to enter in the list:  "))
    
    for i in range(Num):
        Elements = int(input("Enter the elements:   "))
        Mylist.append(Elements)

    print("The entered list is: ",Mylist)

    FData = list(filter(EvenData, Mylist))
    print("The even numbers are:    ",FData)

    MData = list(map(SquareData, FData))
    print("Square of elements:  ",MData)

    RData = reduce(AddData, MData)
    print("The addition of elements:    ",RData)

if __name__ == "__main__":
    main()
