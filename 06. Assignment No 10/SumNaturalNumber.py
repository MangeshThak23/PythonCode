#2. Write a program which accepts one number and prints sum of first N natural numbers.

def Natural(No1):
    Ans=0
    for i in range(1,No1+1):
        Ans = Ans+i

    print(Ans)

if __name__ == "__main__":
    Num1= int(input("Enter a number:"))
    Natural(Num1)