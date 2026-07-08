"""3. Write a program which accept one number from user and return its factorial."""

def Factorial(No):
    Fact=1
    for i in range(1,No+1):
        Fact = Fact * i
    return Fact
def main():
   Num = int(input("Enter a number:     "))
   Ret= Factorial(Num)
   
   print(f"Factorial of {Num} is:   ",Ret)

if __name__ == "__main__":
   main()
