#5. Write a lambda function which accepts one number and returns True if number is even otherwise False.

Even = lambda No : No % 2 == 0

def main():
    Num = int(input("Enter a number:"))
    Ret = Even(Num)
    print("The number is:", Ret)

if __name__ == "__main__":
    main()