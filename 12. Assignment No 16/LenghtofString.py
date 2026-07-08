"""10. Write a program which accept name from user and display length of its name."""

def Name():

    Char = str(input("Enter a name: "))
    Count = 0
    for i in Char:
        Count += 1
    print(Count)


def main():
    
    Name()

if __name__ == "__main__":
    main()

