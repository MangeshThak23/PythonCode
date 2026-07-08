"""5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime()."""

import MarvellousNum

def ListPrime():
    Mylist = []
    ListN = int(input("Enter number of elements:    "))

    for i in range(ListN):
        Elements = int(input("Enter the elements:   "))
        Mylist.append(Elements)

    print(Mylist)

    Sum = 0
    for j in Mylist:
        if MarvellousNum.ChkPrime(j)==True:
            Sum = Sum + j
    print(Sum)


def main():
    ListPrime()

if __name__ == "__main__":
    main()
    