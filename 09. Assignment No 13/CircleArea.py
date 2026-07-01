#2. Write a program which accepts radius of circle and prints area of circle.

Area = lambda r : 3.14*(r*r)

def main():
    Radius1 = float(input("Enter radius of circle:"))
    Ret= Area(Radius1)
    print("Area of circle is:",Ret)

if __name__ == "__main__":
    main()