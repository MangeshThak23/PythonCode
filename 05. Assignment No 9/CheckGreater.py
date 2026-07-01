#2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

def ChkGreater(No1, No2):
    if No1>No2:
        print(No1, "is greater than ", No2)
    elif No1<No2:
         print(No2, "is greater than ", No1)
    else:
        print("Both numbers are equal.")

if __name__ == "__main__":
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))
    ChkGreater(Num1, Num2)
    