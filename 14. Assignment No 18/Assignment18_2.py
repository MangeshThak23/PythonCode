"""2.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List."""

from functools import reduce

Maximum = lambda No1, No2 : No1 if No1>No2 else No2

def NumMax(No):
    Mylist = []

    for i in range(No):
        Num = int(input("Enter the number to add in the list:   "))
        Mylist.append(Num)
    print("The entered list:    ", Mylist)

    MData = reduce(Maximum,Mylist)
    print("The maximum number from the list is: ",MData)

def main():
    NumList = int(input("Enter the how much numbers do you want to add in the list: "))
    NumMax(NumList)

if __name__ == "__main__":
    main()