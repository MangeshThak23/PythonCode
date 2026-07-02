# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even
# numbers.

EvenNum = lambda No : No % 2 == 0

def main():
    Mylist = []
    Num = int(input("Enter how much numbers you want to insert in the list:"))

    for i in range(Num):
        Numbers = int(input("Ente the numbers:  "))
        Mylist.append(Numbers)

    print("The entered list is: ", Mylist)

    FData = list(filter(EvenNum,Mylist))
    print("After the filter Even numbers:   ",FData)
    
if __name__ == "__main__":
    main()