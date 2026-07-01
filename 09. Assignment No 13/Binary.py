#4. Write a program which accepts one number and prints binary equivalent.

def Number(No):
    reverse = 0 
    Binary = ""
    while int(No) > 0:
        Digit = int(No) % 2
        No = int(No)/2
        Binary = Binary + str(Digit)        #concatenate
    
    count = len(Binary)
    while count != 0:
        Result = int(Binary) % 10
        reverse = reverse * 10 + Result
        Binary = int(Binary) / 10
        count = count - 1
    return reverse

def main():
    Num = int(input("Enter a number:"))
    Ret = Number(Num)
    print(Ret)

if __name__ == "__main__":
    main()