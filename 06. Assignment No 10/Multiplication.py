#1. Write a program which accepts one number and prints multiplication table of that number.

def Multiplication(No1):
    for i in range(1,11):
        Ans= No1*i
        print(No1,"*",i,"=",Ans)

if __name__ == "__main__":
    Num1 = int(input("Enter a number:"))
    Multiplication(Num1)
