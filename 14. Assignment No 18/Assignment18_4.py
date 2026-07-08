"""4.Write a program which accept N numbers from user and store it into List. Accept one 
another number from user and return frequency of that number from List."""

def FreqNum(No):
    
    Mylist = []

    for i in range(No):
        Num = int(input("Elements:  "))
        Mylist.append(Num)
    print("The entered list is: ",Mylist)

    Num1= int(input("Element to search:  "))
    
    Freq = 0
    for j in Mylist:
        if(j == Num1):
            Freq = Freq + 1
    print(Freq)
    
def main():
    ListNum = int(input("Number of elements:  "))
    FreqNum(ListNum)

if __name__ == "__main__":
    main()



