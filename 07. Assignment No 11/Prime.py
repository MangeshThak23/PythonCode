#1. Write a program which accepts one number and checks whether it is prime or not.

def Prime(No):
    if No<=1:
        print("Enter a number which is greater than 1.")
        return
    
    for i in range(2,(No//2)+1):
        if No %i == 0:
            print("Not Prime number.")
            break
    else:
            print("Prime number.")
    
if __name__ == "__main__":
    Num=int(input("Enter a number:"))
    Prime(Num)