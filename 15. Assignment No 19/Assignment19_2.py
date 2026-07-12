"""2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication."""

Mult = lambda No1,No2 : No1 * No2

def main():
    Num1 = int(input("Enter 1st number:  "))
    Num2 = int(input("Enter 2nd number:  "))
    Ret = Mult(Num1,Num2)
    print("Ans: ",Ret)

if __name__ == "__main__":
    main()
    