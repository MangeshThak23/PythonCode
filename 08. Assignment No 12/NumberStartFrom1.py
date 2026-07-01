#4. Write a program which accepts one number and prints that many numbers starting from 1.

def main():
    Num = int(input("Enter a number:"))
    for i in range(1,Num+1):
        print("The numbers:",i)
    
if __name__ == "__main__":
    main()