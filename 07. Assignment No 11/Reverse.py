# 4. Write a program which accepts one number and prints reverse of that number.

def Reverse(No):
    reverse=0
    while int (No) > 0:
        digit = int(No) % 10
        reverse = reverse * 10 + digit
        No = int(No) / 10
    return reverse

def main():
    Num1 = int(input("Enter number:"))
    Ret = Reverse(Num1)
    print("Reverse:",Ret)
    
if __name__ == "__main__":
     main()