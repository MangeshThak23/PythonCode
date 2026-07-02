# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

OddList = lambda No : No % 2 != 0

def main():
    Num = int(input("Enter the how much numbers do you want in list?  "))
    Mylist = []

    for i in range(Num):
        Numbers = int(input("Enter the number: "))
        Mylist.append(Numbers)

    print("The entered list is: ", Mylist)

    FData = list(filter(OddList, Mylist))
    print("The odd numbers from the list is: ", FData)

if __name__ == "__main__":
    main()