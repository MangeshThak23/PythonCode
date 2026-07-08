"""8. Write a program which accept number from user and print that number of “*” on screen."""

def Star(No):
    for i in range(No):
        print("*")

def main():
    Num = int(input("Enter a number:    "))
    Star(Num)

if __name__ == "__main__":
    main()