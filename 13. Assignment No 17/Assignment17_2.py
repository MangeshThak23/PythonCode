"""2. Write a program which accept one number and display below pattern."""

def Display(No):
    
    for i in range(No):
        for j in range(No):
            print("*",end=" ")
        print()
        
    

def main():
    Num = int(input("Enter a number:    "))
    Display(Num)

if __name__ == "__main__":
    main()