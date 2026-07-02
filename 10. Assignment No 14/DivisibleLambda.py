#7. Write a lambda function which accepts one number and returns True if divisible by 5.

Divisible = lambda No : No % 5 == 0

def main():
    Num = int(input("Enter a number:"))
    Ret = Divisible(Num)
    print("The number is divisible by 5?:",Ret)

if __name__ == "__main__":
    main()