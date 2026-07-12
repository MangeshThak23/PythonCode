"""3.Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. List contains the numbers which 
are accepted from user. 
Filter should filter out all such numbers which greater than or equal to 70 and 
less than or equal to 90. 
Map function will increase each number by 10. 
Reduce will return product of all that numbers."""

from functools import reduce

FilteredData = lambda No : No>= 70 and No <= 90
MapData = lambda No : No + 10
ReduceData = lambda No1, No2 : No1 * No2

def main():
    
    Mylist = []
    
    ListNum = int(input("Enter how much elements you want to enter in the list:  "))
    
    for i in range(ListNum):
        Elements = int(input("Enter the elements:   "))
        Mylist.append(Elements)
    print("The entered list is: ",Mylist)

    FData = list(filter(FilteredData,Mylist))
    print("Filter Data: ",FData)

    MData= list(map(MapData,FData))
    print("After map:   ",MData)

    RData = reduce(ReduceData,MData)
    print("Product of all numbers:  ",RData)

if __name__ == "__main__":
    main()
