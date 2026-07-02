#4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

AddList = lambda No1, No2 : No1 + No2

def main():
    Mylist = [10,20,30,40,50]
    #Num = int(input("Enter how much numbers do you want in a list"))

    #for i in range(Num):
    #    Numbers = int(input("Enter the numbers:"))
    #    Mylist.append(Numbers)
    #    print("The entered list is: ", Mylist)

    print("The list is:",Mylist)
    RData = reduce(AddList, Mylist)
    print("The addition is: ", RData)

if __name__ == "__main__":
    main()   
