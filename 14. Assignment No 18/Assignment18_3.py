"""3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List."""

from functools import reduce

MinNum = lambda No1,No2 : No1 if No1<No2 else No2

def MinFind(No):
    
    Mylist = []

    for i in range(No):
        Num = int(input("Enter the number to add in a list: "))
        Mylist.append(Num)
    print("The entered list is: ",Mylist)

    RData = reduce(MinNum,Mylist)
    print("The minimum number from the list is: ",RData)

def main():
    ListNum = int(input("Enter how much numbers do you want to enter in a list: "))
    MinFind(ListNum)

if __name__ == "__main__":
    main()

    