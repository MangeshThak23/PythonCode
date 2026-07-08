"""1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List."""

from functools import reduce

Add = lambda No1, No2 : No1 + No2

def ElementAdd(No):
    Mylist = []
    
    for i in range(No):
        Num = int(input("Enter a number to add in a list:   "))
        Mylist.append(Num)
    print("The list:    ",Mylist)
    
    RData = reduce(Add, Mylist)
    
    print("The total is:    ", RData)

def main():
    No1 = int(input("Enter how much numbers do you want to add in a list:    "))
    ElementAdd(No1)   

if __name__ == "__main__":
    main()




