#1. Write a program which accepts length and width of rectangle and prints area.

Area = lambda l,w : l*w

def main():
    lenght= float(input("Enter lenght:"))
    width= float(input("Enter width:"))
    Ret = Area(lenght, width)
    print("Area:",Ret)

if __name__ == "__main__":
    main()
