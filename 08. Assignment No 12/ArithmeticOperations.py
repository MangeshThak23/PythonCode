# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.


Addition = lambda No1, No2 : No1 + No2
Substraction = lambda No1, No2 : No1 - No2
Multiplication = lambda No1, No2 : No1 * No2
Division = lambda No1, No2 : No1 / No2

def main():
    Num1 = int(input("Enter first number"))
    Num2 = int(input("Enter seccond number"))

    Add1 = Addition(Num1, Num2)
    Sub1 = Substraction(Num1, Num2)
    Mult1 = Multiplication(Num1, Num2)
    Div1 = Division(Num1, Num2)
    
    print("Addition is:",Add1)
    print("Substraction is:",Sub1)
    print("Multiplication is:",Mult1)
    print("Division is:",Div1)

if __name__ == "__main__":
    main()