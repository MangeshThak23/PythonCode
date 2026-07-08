"""7. Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false."""

def Divisible(No):
    if No % 5 == 0:
        print("True")
    else:
        print("False")

def main():
    Num = int(input("Enter a number:    "))
    Divisible(Num)
    
if __name__ == "__main__":
    main()
