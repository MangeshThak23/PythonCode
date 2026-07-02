#9. Write a lambda function which accepts two numbers and returns multiplication.

Mult = lambda No1, No2 : No1 * No2

def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    Ret = Mult(Num1,Num2)
    print("The multiplication is:",Ret)

if __name__ == "__main__":
    main()