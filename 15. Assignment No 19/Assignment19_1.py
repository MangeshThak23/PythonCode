""""1.Write a program which contains one lambda function which accepts one parameter and return
power of two."""

Power = lambda No : 2**No

def main():
    Num = int(input("Enter a number:    "))
    Ret = Power(Num)
    print(Ret)

if __name__ == "__main__":
    main()
