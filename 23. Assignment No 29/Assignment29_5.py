"""Q5) Frequency of a String in File
Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of
occurrences) of that string in the file."""

def main():
    Fname = input("Enter file name: ")
    String1 = input("Enter a string: ")
    frequency = 0
    word = ""

    try:
        
        fobj = open(Fname,"r")
        
        for line in fobj:
            for ch in line:
                if ch != " " and ch != "\n" and ch != "\t":                 
                    word = word + ch
                else:
                    if word == String1:
                        frequency = frequency+1
                    word = ""
        if word == String1:
            frequency = frequency+1

        fobj.close()

        print(frequency)
    except Exception as ex:
        print("There is no such file")

if __name__ == "__main__":
    main()