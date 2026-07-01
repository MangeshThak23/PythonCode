#5. Write a program which accepts one number and prints that many numbers in reverse order.

def main():
    Num = int(input("Enter a number:"))
    for i in range(Num,0,-1):
        print("The reverse numbers:",i)
    
if __name__ == "__main__":
    main()