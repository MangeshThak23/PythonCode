#4. Write a program which accepts one number and prints all even numbers till that number.

def Even(No):
   if No < 2 :
    print("Enter number which is more than 2")
    return
   
   for i in range(1,No+1):
     if i%2 == 0:
        print(i)
   
if __name__ == "__main__":
  Num=int(input("Enter a number"))
  Even(Num)