"""Q2) Count Words in a File
Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file."""

def main():

    try:
        fname = input("Enter file name: ")

        fobj = open(fname,"r")

        Data = fobj.read()
        words = Data.split()
        CountWords = len(words)
        fobj.close
        print("Words in file: ",CountWords)

    except Exception as ex:
        print("File not available.",ex)

if __name__ == "__main__":
    main() 