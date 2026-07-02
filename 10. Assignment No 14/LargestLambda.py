#10. Write a lambda function which accepts three numbers and returns largest number.

Largest = lambda No1,No2,No3 : No1 if ((No1>=No2)and(No1>=No3)) else (No2 if No2>=No3 else No3)

def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    Num3 = int(input("Enter third number:"))

    Ret = Largest(Num1,Num2,Num3)
    print("The largest number is:",Ret)

if __name__ == "__main__":
    main()