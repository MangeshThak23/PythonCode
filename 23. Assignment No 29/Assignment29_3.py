"""Q3) Copy File Contents into a New File (Command Line)
Problem Statement:
Write a program which accepts an existing file name through command line arguments, creates a new file
named Demo.txt, and copies all contents from the given file into Demo.txt."""

import sys

def main():
    try:
        if(len(sys.argv) >= 2):
            Source_fname = (sys.argv[1])
            dest_fname = "Demo.txt"
    

            fobj = open(Source_fname,"r")
            Data = fobj.read()
            fobj.close()

            fobj1 = open(dest_fname,"w")
            fobj1.write(Data)
            
            fobj1.close()

            print("Done")
        else:
            print("Provide source file name")

    except FileNotFoundError as ex:
       print("There is no such file")

if __name__ == "__main__":
    main()