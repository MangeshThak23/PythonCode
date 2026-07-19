"""Q1) Count Lines in a File
Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file."""

def main():
    try:
        fname = input("Enter file name: ")

        fobj = open(fname,"r")
        print("File gets opend")

        LineCount = 0
        for line in fobj:
            LineCount += 1

             
        print("Total lines in file: ",LineCount)

        fobj.close()

    except Exception as ex:
        print("File is not available",ex)

if __name__ == "__main__":
    main()
