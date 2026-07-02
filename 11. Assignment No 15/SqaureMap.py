#1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

ListMap = lambda No : No**2

def main():
    Num = int(input("Enter how much numbers do you want to enter:"))
    Mylist = []

    for i in range(Num):
        Numbers= int(input("Enter the numbers:"))
        Mylist.append(Numbers)

    print("The list is:",Mylist)

    MData = list(map(ListMap, Mylist))
    print("The square of numbers:",MData)

if __name__ == "__main__":
    main()