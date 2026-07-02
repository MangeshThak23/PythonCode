# 8. Write a lambda function which accepts two numbers and returns addition.

Addition = lambda No1,No2 : No1 + No2

def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))

    Ret = Addition(Num1, Num2)
    print("Addition of these two numbers is:",Ret)

if __name__ == "__main__":
    main()