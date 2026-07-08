"""4.Write a program which accept one number form user and return addition of its factors."""

def Factors(No):
    total = 0
    for i in range(1,No):
        if (No % i) == 0:
            total +=i
    return total

def main():
    Num = int(input("Enter a number:    "))
    Ret=Factors(Num)
    print(f"The factor of {Num} is: ",Ret)
if __name__ == "__main__":
    main()