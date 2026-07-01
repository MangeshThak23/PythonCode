#2.Write a program which accepts one number and prints count of digits in that number.---- Query


def CountDigits(No1):
    if No1 < 0:
        print("Enter corerct number.")
        return
    if No1 == 0:
        print("total digit is: 1")
        return
  
    count=0
    
    while No1 > 0:
        count = count + 1
        No1 = No1 // 10
    print("total digits",count)

if __name__ == "__main__":
    num=int(input("Enter number"))
    CountDigits(num)