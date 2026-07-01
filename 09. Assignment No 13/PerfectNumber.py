#3. Write a program which accepts one number and checks whether it is perfect number or not.

def main():
    Num = int(input("Enter a number:"))
    Sum = 0
    for i in range(1,Num):
        if Num % i == 0:
            Sum +=i
    if Sum == Num:
        print("Perfect number.")
    else:
        print("Not perfect number.")


if __name__ == "__main__":
    main()