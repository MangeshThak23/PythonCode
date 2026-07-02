#6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.

OddN = lambda No : No % 2 != 0

def main():
    Num = int(input("Enter a number:"))
    Ret = OddN(Num)
    print("The entered number is:", Ret)

if __name__ == "__main__":
    main()