#2. Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda No : No**3

def main():
    Num = int(input("Enter a number:"))
    Ret = Cube(Num)
    print("The cube of",Num,"is:",Ret)

if __name__ == "__main__":
    main()