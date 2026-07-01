#3. Write a program which accepts one number and prints factorial of that number.

def Factorial(No):
    if No < 0:
        print("Please enter positive number.")
        return
    
    Ans = 1
    for i in range(1, No+1):
        Ans=Ans * i
    print(Ans)

if __name__ == "__main__":
    Num=int(input("Enter number:"))
    Factorial(Num)
    