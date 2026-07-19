"""Q4) Compare Two Files (Command Line)
Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of
both files.
• If both files contain the same contents, display Success
• Otherwise display Failure"""

import sys

def main():
    if len(sys.argv) >= 2:
        First_fname = sys.argv[1]
        Second_fname = sys.argv[2]
    try:
        fobj1 = open(First_fname,"r")
        Data1 = fobj1.read()
        fobj1.close()

        fobj2 = open(Second_fname,"r")
        Data2 = fobj2.read()
        fobj2.close()

        if (Data1 == Data2):
            print("Sucess")
        else:
            print("Failure")
    except Exception as ex:
        print("No such file in current directory")

if __name__ == "__main__":
    main()
        