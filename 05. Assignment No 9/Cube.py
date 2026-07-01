#4. Write a program which accepts one number and prints cube of that number.

#No1 = int(input("Enter a number: "))
#Ans = No1*No1*No1
#print("The cube of ",No1," is: ",Ans)

def Cube(No1):
    Ans = No1*No1*No1
    print("The cube of",No1,"is: ",Ans)

if __name__ == "__main__":
    Num1 = int(input("Enter a number: "))
    Cube(Num1)