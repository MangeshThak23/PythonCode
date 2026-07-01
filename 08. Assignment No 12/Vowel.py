#1. Write a program which accepts one character and checks whether it is vowel or consonant.####

def Vowel(Ch):
    Charcter = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    return Ch in Charcter
    
def main():
    Ch1=input("Enter one charcter:")
    if len(Ch1) !=1:
        print("Enter correct character")
        return
    if Vowel(Ch1):
        print("Vowels")
    else:
        print("Consonant")
    return

if __name__ == "__main__":
    main()


