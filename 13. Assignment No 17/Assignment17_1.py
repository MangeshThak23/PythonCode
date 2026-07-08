"""1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user."""

from Arithmetic import Add,Sub,Div,Mult

def main():
    Num1 = int(input("Enter first number:   ")) 
    Num2 = int(input("Enter second number:   "))

    Add(Num1,Num2)
    Sub(Num1,Num2)
    Mult(Num1,Num2)
    Div(Num1,Num2)

if __name__ == "__main__":
    main()