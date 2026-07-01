# 3. Write a program which accepts one number and prints sum of digits.

def main():
    
    Num1 = int(input("Enter number:"))
    if Num1 < 0:
        print("Enter number greater than 0")
       
    elif Num1 > 0:
        SumOfDigits = 0
        while Num1 > 0:
            remainder = Num1 % 10
            Num1 = Num1 // 10
            SumOfDigits = SumOfDigits + remainder
        print(SumOfDigits)
    return 

if __name__ == "__main__":
     main()