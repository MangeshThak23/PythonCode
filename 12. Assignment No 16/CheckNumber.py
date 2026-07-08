"""2. Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console."""

def ChkNum(No):
    
    if (No % 2 == 0):
        print(f"{No} is an even number.")
    else:
        print(f"{No} is an odd number.")

def main():
    Num = int(input("Enter a number:    "))
    ChkNum(Num)
   
if __name__ == "__main__":
    main()