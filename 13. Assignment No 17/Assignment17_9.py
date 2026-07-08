"""9. Write a program which accept number from user and return number of digits 
in that number."""

def NumDigits(No):
    Count = 0
    if No==0:
        print("1")
        return 
   
    if No<0:
        No=No*-1
       
    while No>0:
        Count=Count+1
        No=No//10
    print(Count)

def main():
    Num = int(input("Enter the numbers:    "))
    NumDigits(Num)
    

if __name__ == "__main__":
    main()