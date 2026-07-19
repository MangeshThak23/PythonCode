"""Q5) Search a Word in File
Problem Statement:
Write a program which accepts a file name and a word from the user and checks whether that word is present in
the file or not."""

def main():
   
    fname1 = input("Enter file name: ")
    word1 = input("Enter a word: ")

    try:

        fobj = open(fname1,"r")
        Data = fobj.read()

        if word1 in Data:
            print(f"The {word1} is present in {fname1} file.")
        else:
            print(f"The {word1} is not present in {fname1} file.")

        fobj.close()
    except Exception as ex:
        print("There is no such file.")
if __name__ == "__main__":
    main()