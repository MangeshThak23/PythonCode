"""Q1) Check File Exists in Current Directory
Problem Statement:
Write a program which accepts a file name from the user and checks whether that file exists in the current
directory or not."""

import os

def main():
    fname = input("Enter a file name:   ")
    if(os.path.exists(fname)):
        print("File exists in current directory")
    else:
        print("File does not exists in current directory")
            
if __name__ == "__main__":
    main()    
