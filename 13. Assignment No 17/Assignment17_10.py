"""10. Write a program which accept number from user and return addition of digits in that number."""

def Addition(No):
    Count = 0
    while No>0:
       Rem = No % 10
       Count += Rem
       No = No //10
    print(Count)
           
def main():
    Num = int(input("Enter a number:    "))
    Addition(Num)

if __name__ == "__main__":
    main()