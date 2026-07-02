#4. Write a lambda function which accepts two numbers and returns minimum number.

Min = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    Ret = Min(Num1,Num2)
    print("The min number is:",Ret)

if __name__ == "__main__":
    main()
    