# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

Mult = lambda No1,No2 : No1 * No2

def main():
    Mylist = []
    Num = int(input("Enter the numbers do you want to enter in the list: "))
    
    for i in range(Num):
        Numbers = int(input("Enter the number: "))
        Mylist.append(Numbers)

    print("The list is: ",Mylist)

    RData = reduce(Mult, Mylist)
    print("After reduce:    ",RData)

if __name__ == "__main__":
    main()