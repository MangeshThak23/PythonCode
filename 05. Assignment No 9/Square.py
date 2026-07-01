#3. Write a program which accepts one number and prints square of that number.

#No1 = int(input("Enter a number: "))
#Ans = No1*No1
#print("The square of ",No1," is: ",Ans)

def Square(No1):
    Ans= No1 * No1
    print("The square of",No1, "is: ",Ans)

if __name__ == "__main__":
    Num1 = int(input("Enter one number: "))
    Square(Num1)