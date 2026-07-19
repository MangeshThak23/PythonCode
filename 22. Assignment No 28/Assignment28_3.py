"""Q3) Display File Line by Line
Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the
screen."""

def main():
    try:
        fname = input("Enter file name: ")

        fobj = open(fname,"r")

        Data = fobj.read()
        print(Data)
        fobj.close
    
    except FileNotFoundError as fe:
         print("File not found.",fe)

if __name__ == "__main__":
        main()
    