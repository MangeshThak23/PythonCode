#3. Write a lambda function which accepts two numbers and returns maximum number.

Max = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    Ret = Max(Num1,Num2)
    print("The max number is:",Ret)

if __name__ == "__main__":
    main()