#2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

ListEven = lambda No : No % 2 == 0

def main():
    Mylist = []
    Num = int(input("Enter the number of list?"))

    for i in range(Num):
        Numbers = int(input("Enter the numbers:"))
        Mylist.append(Numbers)

    print("The entered list is:",Mylist)

    FData = list(filter(ListEven,Mylist))
    print("The even numbers are :",FData)

if __name__ == "__main__":
    main()
