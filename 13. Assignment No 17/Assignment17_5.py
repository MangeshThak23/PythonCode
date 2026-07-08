"""5.Write a program which accept one number for user and check whether number is prime or not."""

def PrimeNum(No):
    if No <= 1:
        print("The entered number is not prime.")
        return
    for i in range(2,No):
        if No % i == 0:
            print("The entered number is not prime.")
            return
    print("The entered number is prime.")


def main():
    Num = int(input("Enter a number:    "))
    PrimeNum(Num)
    
if __name__ == "__main__":
    main()