"""6.Write a program which accept number from user and check whether that number is positive or
negative or zero."""

def CheckNum(No):
    if No==0:
        print("The entered number is zero")
    elif No>0:
        print("The entered number is positive")
    else:
        print("The entered number is negative")

def main():
    Num = int(input("Enter a number: "))
    CheckNum(Num)

if __name__ == "__main__":
    main()
