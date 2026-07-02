#5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

MaxList = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    #Mylist = [10,20,100,50,600]

    Num = int(input("Enter the how much numbers do you want in list?  "))
    Mylist = []

    for i in range(Num):
        Numbers = float(input("Enter the number: "))
        Mylist.append(Numbers)

    print("The entered list is: ", Mylist)

    RData = reduce(MaxList,Mylist)
    print("Reduce data:", RData)

if __name__ == "__main__":
    main()

    