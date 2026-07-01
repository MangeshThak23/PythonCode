#5. Write a program which accepts one number and checks whether it is divisible by 3 and 5

def Divisible(No1):
    if No1%3==0 and No1%5==0:
        print("Entered number is divisible by 3 and 5.")
    else:
        print("Entered number is not divisible by 3 and 5.")

if __name__ == "__main__":
    Num1 = int(input("Enter number: "))
    Divisible(Num1)