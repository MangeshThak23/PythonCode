"""Q2) Display File Contents
Problem Statement:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
console."""

def main():
    fname = input("Enter a file name: ")

    try:
        fobj = open(fname,"r")
        Data = fobj.read()

        print(Data)
    
    except FileNotFoundError as ex:
        print("There is no such file.")

    
if __name__ == "__main__":
    main()