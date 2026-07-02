#1. Write a lambda function which accepts one number and returns square of that number.

Square = lambda No : No*No

def main():
    Num = int(input("Enter a number:"))
    Ret = Square(Num)
    print("The square of",Num,"is:",Ret)

if __name__ == "__main__":
    main()