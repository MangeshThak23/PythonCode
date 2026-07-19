"""Q4) Copy File Contents into Another File
Problem Statement:
Write a program which accepts two file names from the user.
• First file is an existing file
• Second file is a new file
Copy all contents from the first file into the second file."""

def main():
    try:
        fname1 = input("Enter extisting file name: ")
        fname2 = input("Enter new file name: ")


        fobj1 = open(fname1,"r")
        Data1 = fobj1.read()

        fobj2 = open(fname2,"w")
        Data2 = fobj2.write(Data1)

        fobj1.close
        fobj2.close
        
        print("File copied")
    
    except Exception as ex:
        print("Exception",ex)


if __name__ == "__main__":
    main()


