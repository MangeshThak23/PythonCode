#6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

MinReduce = lambda No1, No2 : No1 if No1 < No2  else No2

def main():
    Mylist = []
    Numbers = int(input("Enter how much numbers do you want in list:"))
    
    for i in range(Numbers):
        Num = int(input("Enter the numbers: "))
        Mylist.append(Num)

    print("The list is :",Mylist)

    RData = reduce(MinReduce, Mylist)
    print("The min number is: ", RData)

if __name__ == "__main__":
    main()