"""Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers."""

def Add(No1, No2):
    Ans = No1 + No2

    print(f"The addition of {No1} and {No2} is: ", Ans)

def main():
    Num1 = int(input("Enter first number:    "))
    Num2 = int(input("Enter second number:    "))

    Add(Num1,Num2)

if __name__ == "__main__":
    main()